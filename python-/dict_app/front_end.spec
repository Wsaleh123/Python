# -*- mode: python -*-

block_cipher = None


a = Analysis(['front_end.py'],
             pathex=['C:\\Users\\wesam\\Documents\\Personal\\Coding\\dict_app'],
             binaries=[],
             datas=[],
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
          name='front_end',
          debug=False,
          strip=False,
          upx=True,
          console=False )
