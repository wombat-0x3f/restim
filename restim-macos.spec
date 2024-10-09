# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['restim.py'],
    pathex=['.'],
    binaries=[],
    datas=[('resources/phase diagram bg.svg', 'resources/'), ('resources/favicon.png', 'resources/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    name='restim',
    exclude_binaries=True,
    manifest=None,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='restim',
)

app = BUNDLE(
    coll,
    name='restim.app',
    icon='resources/favicon.png',
    bundle_identifier=None,
)