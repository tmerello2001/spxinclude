#!/bin/python3
# coding: utf-8


import os

from sphinx.directives import other
from sphinx.util import logging
from git import Repo

from spxinclude import __version__

logger = logging.getLogger(__name__)


class GitRemoteInclude(other.Include):
    """Create git-remote-include directive."""

    def run(self):
        """Return rel path to a downloaded file as `include` node argument."""
        document = self.state.document
        env = document.settings.env
        buildpath = env.app.outdir

        args = self.arguments[0].split(',&')

        try:
            downloadpath = os.path.join(buildpath, "_downloads")
            repopath = os.path.join(downloadpath, args[0])
            if not os.path.isdir(downloadpath):
                os.makedirs(downloadpath)
            Repo.clone_from(args[0], repopath, branch=args[1])

            rstfile = os.path.join(repopath, os.path.basename(args[2]))

            with open(rstfile, 'r') as srcfile:
                target_content = srcfile.read()
                with open(env.doc2path(env.docname), "w") as destfile:
                    destfile.write(target_content)

            self.arguments = [rstfile]
            return super(GitRemoteInclude, self).run()

        except Exception as e:
            return [document.reporter.warning(str(e), line=self.lineno)]


def setup(app):
    """
    Set up Sphinx extension.
    :param app: Sphinx application context.
    """
    logger.info("adding git-remote-include directive...", nonl=True)
    app.add_directive("git-remote-include", GitRemoteInclude)
    logger.info(" done")
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


if __name__ == "__main__":
    pass
