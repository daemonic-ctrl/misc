# -*- mode: python -*-

block_cipher = None


a = Analysis(['tester_test.py'],
             pathex=['/root/Programs/python3_programs'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='tester_test',
          debug=False,
          strip=False,
          upx=True,
          console=True )
