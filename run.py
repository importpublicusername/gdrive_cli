import fire
from loguru import logger

import restore_trash

class Actions(object):
    def trash_restore(self):
        '''restores all items currently in the trash'''
        logger.info('restoring trash')
        restore_trash.main()

    def trash_delete(self):
        '''not implemented'''
        logger.warning('trash_delete not implemented')

if __name__ == '__main__':
     fire.Fire(Actions())
