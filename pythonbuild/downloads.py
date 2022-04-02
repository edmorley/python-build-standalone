# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

DOWNLOADS = {
    # 6.0.19 is the last version licensed under the Sleepycat license.
    "bdb": {
        "url": "https://ftp.osuosl.org/pub/blfs/conglomeration/db/db-6.0.19.tar.gz",
        "size": 36541923,
        "sha256": "2917c28f60903908c2ca4587ded1363b812c4e830a5326aaa77c9879d13ae18e",
        "version": "6.0.19",
        "library_names": ["db"],
        "licenses": ["Sleepycat"],
        "license_file": "LICENSE.bdb.txt",
    },
    "binutils": {
        "url": "https://ftp.gnu.org/gnu/binutils/binutils-2.38.tar.xz",
        "size": 23651408,
        "sha256": "e316477a914f567eccc34d5d29785b8b0f5a10208d36bbacedcc39048ecfe024",
        "version": "2.38",
    },
    "bzip2": {
        "url": "https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz",
        "size": 810029,
        "sha256": "ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269",
        "version": "1.0.8",
        "library_names": ["bz2"],
        "licenses": ["bzip2-1.0.6"],
        "license_file": "LICENSE.bzip2.txt",
    },
    "clang": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-13.0.1/clang-13.0.1.src.tar.xz",
        "size": 17847584,
        "sha256": "787a9e2d99f5c8720aa1773e4be009461cd30d3bd40fdd24591e473467c917c9",
        "version": "13.0.1",
    },
    "clang-compiler-rt": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-13.0.1/compiler-rt-13.0.1.src.tar.xz",
        "size": 2290068,
        "sha256": "7b33955031f9a9c5d63077dedb0f99d77e4e7c996266952c1cec55626dca5dfc",
        "version": "13.0.1",
    },
    "cmake-linux-bin": {
        "url": "https://github.com/Kitware/CMake/releases/download/v3.19.2/cmake-3.19.2-Linux-x86_64.tar.gz",
        "size": 42931014,
        "sha256": "4d8a6d852c530f263b22479aad196416bb4406447e918bd9759c6593b7f5f3f9",
        "version": "3.19.2",
    },
    "cmake-macos-bin": {
        "url": "https://github.com/Kitware/CMake/releases/download/v3.19.2/cmake-3.19.2-macos-universal.tar.gz",
        "size": 63739197,
        "sha256": "50afa2cb66bea6a0314ef28034f3ff1647325e30cf5940f97906a56fd9640bd8",
        "version": "3.19.2",
    },
    "cpython-3.8": {
        "url": "https://www.python.org/ftp/python/3.8.13/Python-3.8.13.tar.xz",
        "size": 19023016,
        "sha256": "6f309077012040aa39fe8f0c61db8c0fa1c45136763299d375c9e5756f09cf57",
        "version": "3.8.13",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp38",
    },
    "cpython-3.9": {
        "url": "https://www.python.org/ftp/python/3.9.12/Python-3.9.12.tar.xz",
        "size": 19740524,
        "sha256": "2cd94b20670e4159c6d9ab57f91dbf255b97d8c1a1451d1c35f4ec1968adf971",
        "version": "3.9.12",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp39",
    },
    "cpython-3.10": {
        "url": "https://www.python.org/ftp/python/3.10.3/Python-3.10.3.tar.xz",
        "size": 19343528,
        "sha256": "596c72de998dc39205bc4f70ef0dbf7edec740a306d09b49a9bd0a77806730dc",
        "version": "3.10.3",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp310",
    },
    "gcc": {
        "url": "https://ftp.gnu.org/gnu/gcc/gcc-10.3.0/gcc-10.3.0.tar.xz",
        "size": 76692288,
        "sha256": "64f404c1a650f27fc33da242e1f2df54952e3963a49e06e73f6940f3223ac344",
        "version": "10.3.0",
    },
    "gdbm": {
        "url": "https://ftp.gnu.org/gnu/gdbm/gdbm-1.21.tar.gz",
        "size": 1005982,
        "sha256": "b0b7dbdefd798de7ddccdd8edf6693a30494f7789777838042991ef107339cc2",
        "version": "1.21",
        "library_names": ["gdbm"],
        "licenses": ["GPL-3.0-or-later"],
        "license_file": "LICENSE.gdbm.txt",
    },
    # gmp 6.2 does not build on wheezy.
    "gmp": {
        "url": "https://ftp.gnu.org/gnu/gmp/gmp-6.1.2.tar.xz",
        "size": 1946336,
        "sha256": "87b565e89a9a684fe4ebeeddb8399dce2599f9c9049854ca8c0dfbdea0e21912",
        "version": "6.1.2",
    },
    "inputproto": {
        "url": "https://www.x.org/archive/individual/proto/inputproto-2.3.2.tar.gz",
        "size": 244334,
        "sha256": "10eaadd531f38f7c92ab59ef0708ca195caf3164a75c4ed99f0c04f2913f6ef3",
        "version": "2.3.2",
    },
    "isl": {
        "url": "https://gcc.gnu.org/pub/gcc/infrastructure/isl-0.18.tar.bz2",
        "size": 1658291,
        "sha256": "6b8b0fd7f81d0a957beb3679c81bbb34ccc7568d5682844d8924424a0dadcb1b",
        "version": "0.18",
    },
    "jom-windows-bin": {
        "url": "http://download.qt.io/official_releases/jom/jom_1_1_3.zip",
        "size": 1213852,
        "sha256": "128fdd846fe24f8594eed37d1d8929a0ea78df563537c0c1b1861a635013fff8",
        "version": "1.1.3",
    },
    "kbproto": {
        "url": "https://www.x.org/archive/individual/proto/kbproto-1.0.7.tar.gz",
        "size": 325858,
        "sha256": "828cb275b91268b1a3ea950d5c0c5eb076c678fdf005d517411f89cc8c3bb416",
        "version": "1.0.7",
    },
    "libc++": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-13.0.1/libcxx-13.0.1.src.tar.xz",
        "size": 2085992,
        "sha256": "2f446acc00bb7cfb4e866c2fa46d1b6dbf4e7d2ab62e3c3d84e56f7b9e28110f",
        "version": "13.0.1",
    },
    "libc++abi": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-13.0.1/libcxxabi-13.0.1.src.tar.xz",
        "size": 554912,
        "sha256": "db5fa6093c786051e8b1c85527240924eceb6c95eeff0a2bbc57be8422b3cef1",
        "version": "13.0.1",
    },
    "libedit": {
        "url": "https://thrysoee.dk/editline/libedit-20210910-3.1.tar.gz",
        "size": 524722,
        "sha256": "6792a6a992050762edcca28ff3318cdb7de37dccf7bc30db59fcd7017eed13c5",
        "version": "20210910-3.1",
        "library_names": ["edit"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libedit.txt",
    },
    # libffi 3.4 has trouble building with musl due to Linux headers wonkiness.
    "libffi": {
        "url": "https://github.com/libffi/libffi/releases/download/v3.3/libffi-3.3.tar.gz",
        "size": 1305466,
        "sha256": "72fba7922703ddfa7a028d513ac15a85c8d54c8d67f55fa5a4802885dc652056",
        "version": "3.3",
        "library_names": ["ffi"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libffi.txt",
    },
    "libpthread-stubs": {
        "url": "https://www.x.org/archive/individual/lib/libpthread-stubs-0.1.tar.gz",
        "size": 301448,
        "sha256": "f8f7ca635fa54bcaef372fd5fd9028f394992a743d73453088fcadc1dbf3a704",
        "version": "0.1",
    },
    "libunwind": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-13.0.1/libunwind-13.0.1.src.tar.xz",
        "size": 99560,
        "sha256": "e206dbf1bbe058a113bffe189386ded99a160b2443ee1e2cd41ff810f78551ba",
        "version": "13.0.1",
    },
    "libX11": {
        "url": "https://www.x.org/archive/individual/lib/libX11-1.6.8.tar.gz",
        "size": 3144482,
        "sha256": "69d1a27cba722dca897198a23fa8d3cad3ec0c715e00205ea4398ec68a4258a5",
        "version": "1.6.8",
        "library_names": ["X11", "X11-xcb"],
        "licenses": ["MIT", "X11"],
        "license_file": "LICENSE.libX11.txt",
    },
    "libXau": {
        "url": "https://www.x.org/releases/individual/lib/libXau-1.0.7.tar.gz",
        "size": 349278,
        "sha256": "cbb81b4ba0f585faac8b9914b0bdbef6e0ef886a30c70d6584e2b30efeda9ac4",
        "version": "1.0.7",
        "library_names": ["Xau"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libXau.txt",
    },
    "libxcb": {
        "url": "https://xcb.freedesktop.org/dist/libxcb-1.13.1.tar.gz",
        "size": 636748,
        "sha256": "f09a76971437780a602303170fd51b5f7474051722bc39d566a272d2c4bde1b5",
        "version": "1.13.1",
        "library_names": ["xcb"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libxcb.txt",
    },
    "lld": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-13.0.1/lld-13.0.1.src.tar.xz",
        "size": 1473868,
        "sha256": "666af745e8bf7b680533b4d18b7a31dc7cab575b1e6e4d261922bbafd9644cfb",
        "version": "13.0.1",
    },
    "llvm": {
        "url": "https://github.com/llvm/llvm-project/releases/download/llvmorg-13.0.1/llvm-13.0.1.src.tar.xz",
        "size": 45479112,
        "sha256": "ec6b80d82c384acad2dc192903a6cf2cdbaffb889b84bfb98da9d71e630fc834",
        "version": "13.0.1",
    },
    "mpc": {
        "url": "http://www.multiprecision.org/downloads/mpc-1.0.3.tar.gz",
        "size": 669925,
        "sha256": "617decc6ea09889fb08ede330917a00b16809b8db88c29c31bfbb49cbf88ecc3",
        "version": "1.0.3",
    },
    # We seem to have problems building newer MPFR in Debian Jessie.
    "mpfr": {
        "url": "https://ftp.gnu.org/gnu/mpfr/mpfr-3.1.6.tar.xz",
        "size": 1133672,
        "sha256": "7a62ac1a04408614fccdc506e4844b10cf0ad2c2b1677097f8f35d3a1344a950",
        "version": "3.1.6",
    },
    "musl": {
        "url": "https://www.musl-libc.org/releases/musl-1.2.2.tar.gz",
        "size": 1055220,
        "sha256": "9b969322012d796dc23dda27a35866034fa67d8fb67e0e2c45c913c3d43219dd",
        "version": "1.2.2",
    },
    "ncurses": {
        "url": "https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.3.tar.gz",
        "size": 3583550,
        "sha256": "97fc51ac2b085d4cde31ef4d2c3122c21abc217e9090a43a30fc5ec21684e059",
        "version": "6.3",
        "library_names": ["ncurses", "ncursesw", "panel", "panelw"],
        "licenses": ["X11"],
        "license_file": "LICENSE.ncurses.txt",
    },
    "ninja-linux-bin": {
        "url": "https://github.com/ninja-build/ninja/releases/download/v1.10.2/ninja-linux.zip",
        "size": 103219,
        "sha256": "763464859c7ef2ea3a0a10f4df40d2025d3bb9438fcb1228404640410c0ec22d",
        "version": "1.10.2",
    },
    "ninja-macos-bin": {
        "url": "https://github.com/ninja-build/ninja/releases/download/v1.10.2/ninja-mac.zip",
        "size": 234089,
        "sha256": "6fa359f491fac7e5185273c6421a000eea6a2f0febf0ac03ac900bd4d80ed2a5",
        "version": "1.10.2",
    },
    "openssl": {
        "url": "https://www.openssl.org/source/openssl-1.1.1n.tar.gz",
        "size": 9850712,
        "sha256": "40dceb51a4f6a5275bde0e6bf20ef4b91bfc32ed57c0552e2e8e15463372b17a",
        "version": "1.1.1n",
        "library_names": ["crypto", "ssl"],
        "licenses": ["OpenSSL"],
        "license_file": "LICENSE.openssl.txt",
    },
    "nasm-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/nasm-2.11.06.tar.gz",
        "size": 384826,
        "sha256": "8af0ae5ceed63fa8a2ded611d44cc341027a91df22aaaa071efedc81437412a5",
        "version": "2.11.06",
    },
    "patchelf": {
        "url": "https://github.com/NixOS/patchelf/releases/download/0.12/patchelf-0.12.tar.bz2",
        "size": 165069,
        "sha256": "699a31cf52211cf5ad6e35a8801eb637bc7f3c43117140426400d67b7babd792",
        "version": "0.12",
    },
    "pip": {
        "url": "https://files.pythonhosted.org/packages/4d/16/0a14ca596f30316efd412a60bdfac02a7259bf8673d4d917dc60b9a21812/pip-22.0.4-py3-none-any.whl",
        "size": 2123599,
        "sha256": "c6aca0f2f081363f689f041d90dab2a07a9a07fb840284db2218117a52da800b",
        "version": "22.0.4",
    },
    "readline": {
        "url": "https://ftp.gnu.org/gnu/readline/readline-8.1.2.tar.gz",
        "size": 2993073,
        "sha256": "7589a2381a8419e68654a47623ce7dfcb756815c8fee726b98f90bf668af7bc6",
        "version": "8.1.2",
        "library_names": ["readline"],
        "licenses": ["GPL-3.0"],
        "license_file": "LICENSE.readline.txt",
    },
    "setuptools": {
        "url": "https://files.pythonhosted.org/packages/3b/02/8d4d27b1cacaac2d129a27d17a22d92a2a5eedcb7817d4ed8ab0d4daf5c4/setuptools-60.9.3-py3-none-any.whl",
        "size": 1078952,
        "sha256": "e4f30b9f84e5ab3decf945113119649fec09c1fc3507c6ebffec75646c56e62b",
        "version": "60.9.3",
    },
    # Remember to update verify_distribution.py when version changed.
    "sqlite": {
        "url": "https://www.sqlite.org/2022/sqlite-autoconf-3380100.tar.gz",
        "size": 3031923,
        "sha256": "8e3a8ceb9794d968399590d2ddf9d5c044a97dd83d38b9613364a245ec8a2fc4",
        "version": "3380100",
        "actual_version": "3.38.1.0",
        "library_names": ["sqlite3"],
        "licenses": [],
        "license_file": "LICENSE.sqlite.txt",
        "license_public_domain": True,
    },
    "strawberryperl": {
        "url": "http://strawberryperl.com/download/5.28.1.1/strawberry-perl-5.28.1.1-32bit-portable.zip",
        "size": 143242779,
        "sha256": "8b15c7c9574989568254a7859e473b7d5f68a1145d2e4418036600a81b13805c",
        "version": "5.28.1.1",
    },
    "tcl": {
        "url": "https://prdownloads.sourceforge.net/tcl/tcl8.6.12-src.tar.gz",
        "size": 10353486,
        "sha256": "26c995dd0f167e48b11961d891ee555f680c175f7173ff8cb829f4ebcde4c1a6",
        "version": "8.6.12",
        "library_names": ["tcl8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tix": {
        "url": "https://github.com/python/cpython-source-deps/archive/tix-8.4.3.6.tar.gz",
        "size": 1836451,
        "sha256": "f7b21d115867a41ae5fd7c635a4c234d3ca25126c3661eb36028c6e25601f85e",
        "version": "8.4.3.6",
        "licenses": ["TCL"],
        "license_file": "LICENSE.tix.txt",
    },
    "tk": {
        "url": "https://prdownloads.sourceforge.net/tcl/tk8.6.12-src.tar.gz",
        "size": 4515393,
        "sha256": "12395c1f3fcb6bed2938689f797ea3cdf41ed5cb6c4766eec8ac949560310630",
        "version": "8.6.12",
        "library_names": ["tk8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tk-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/e3c3e9a2856124aa32b608632a52742d479eb7a9.tar.gz",
        "size": 6787654,
        "sha256": "01ad9c663659224e075d487cbc33ea2fed7a225593965b79bed92ca7f79b676f",
        "version": "8.6.12",
        "git_commit": "e3c3e9a2856124aa32b608632a52742d479eb7a9",
    },
    "uuid": {
        "url": "https://sourceforge.net/projects/libuuid/files/libuuid-1.0.3.tar.gz",
        "size": 318256,
        "sha256": "46af3275291091009ad7f1b899de3d0cea0252737550e7919d17237997db5644",
        "version": "1.0.3",
        "library_names": ["uuid"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libuuid.txt",
    },
    "x11-util-macros": {
        "url": "https://www.x.org/archive/individual/util/util-macros-1.19.2.tar.gz",
        "size": 103001,
        "sha256": "9225c45c3de60faf971979a55a5536f3562baa4b6f02246c23e98ac0c09a75b7",
        "version": "1.19.2",
    },
    "xcb-proto": {
        "url": "https://www.x.org/archive/individual/proto/xcb-proto-1.14.1.tar.gz",
        "size": 194674,
        "sha256": "85cd21e9d9fbc341d0dbf11eace98d55d7db89fda724b0e598855fcddf0944fd",
        "version": "1.14.1",
    },
    "xextproto": {
        "url": "https://www.x.org/archive/individual/proto/xextproto-7.3.0.tar.gz",
        "size": 290814,
        "sha256": "1b1bcdf91221e78c6c33738667a57bd9aaa63d5953174ad8ed9929296741c9f5",
        "version": "7.3.0",
    },
    "xorgproto": {
        "url": "https://www.x.org/archive/individual/proto/xorgproto-2019.1.tar.gz",
        "size": 1119813,
        "sha256": "38ad1d8316515785d53c5162b4b7022918e03c11d72a5bd9df0a176607f42bca",
        "version": "2019.1",
    },
    "xproto": {
        "url": "https://www.x.org/archive/individual/proto/xproto-7.0.31.tar.gz",
        "size": 367979,
        "sha256": "6d755eaae27b45c5cc75529a12855fed5de5969b367ed05003944cf901ed43c7",
        "version": "7.0.31",
    },
    "xtrans": {
        "url": "https://www.x.org/archive/individual/lib/xtrans-1.4.0.tar.gz",
        "size": 225941,
        "sha256": "48ed850ce772fef1b44ca23639b0a57e38884045ed2cbb18ab137ef33ec713f9",
        "version": "1.4.0",
    },
    "xz": {
        "url": "https://tukaani.org/xz/xz-5.2.5.tar.gz",
        "size": 1791345,
        "sha256": "f6f4910fd033078738bd82bfba4f49219d03b17eb0794eb91efbae419f4aba10",
        "version": "5.2.5",
        "library_names": ["lzma"],
        # liblzma is in the public domain. Other parts of code have licenses. But
        # we only use liblzma.
        "licenses": [],
        "license_file": "LICENSE.liblzma.txt",
        "license_public_domain": True,
    },
    "zlib": {
        "url": "https://zlib.net/fossils/zlib-1.2.11.tar.gz",
        "size": 607698,
        "sha256": "c3e5e9fdd5004dcb542feda5ee4f0ff0744628baf8ed2dd5d66f8ca1197cb1a1",
        "version": "1.2.11",
        "library_names": ["z"],
        "licenses": ["Zlib"],
        "license_file": "LICENSE.zlib.txt",
    },
}
