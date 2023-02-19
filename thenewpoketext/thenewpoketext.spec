a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'thenewpoketext.py'],
             pathex=['C:\\Downloads\\pyinstaller-1.3'])
pyz = PYZ(a.pure)
exe = EXE( pyz,
          a.scripts,
          a.binaries,
          name='thenewpoketext.exe',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='app.ico')
