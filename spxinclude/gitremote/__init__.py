#!/bin/python3
# coding: utf-8
import os

from sphinx.directives.other import BaseInclude, SphinxDirective
from sphinx.util import logging
from git import Repo

from spxinclude import __version__

logger = logging.getLogger(__name__)


class GitRemoteInclude(BaseInclude, SphinxDirective):
    """Create git-remote-include directive."""

    def run(self):
        """Include .rst files from Github repositories"""
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

            source = os.path.join(repopath, os.path.basename(args[2]))
            dest = env.doc2path(env.docname)

            target_content = ""
            with open(source, 'r') as srcfile:
                target_content = srcfile.read()
                srcfile.close()

            with open(dest, "w") as destfile:
                destfile.write(target_content)
                destfile.close()

            self.arguments[0] = dest
            return super().run()

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
