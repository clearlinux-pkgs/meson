#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : meson
Version  : 0.46.1
Release  : 22
URL      : https://github.com/mesonbuild/meson/archive/0.46.1.tar.gz
Source0  : https://github.com/mesonbuild/meson/archive/0.46.1.tar.gz
Summary  : jonne2 library
Group    : Development/Tools
License  : Apache-2.0
Requires: meson-bin
Requires: meson-python3
Requires: meson-man
Requires: meson-python
Requires: ninja
BuildRequires : cmake
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : setuptools

%description
ftdetect sets the filetype
syntax does Meson syntax highlighting
plugin does Meson indentation

%package bin
Summary: bin components for the meson package.
Group: Binaries
Requires: meson-man

%description bin
bin components for the meson package.


%package man
Summary: man components for the meson package.
Group: Default

%description man
man components for the meson package.


%package python
Summary: python components for the meson package.
Group: Default
Requires: meson-python3

%description python
python components for the meson package.


%package python3
Summary: python3 components for the meson package.
Group: Default
Requires: python3-core

%description python3
python3 components for the meson package.


%prep
%setup -q -n meson-0.46.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1526570487
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/meson
/usr/bin/mesonconf
/usr/bin/mesonintrospect
/usr/bin/mesontest
/usr/bin/wraptool

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/meson.1
/usr/share/man/man1/mesonconf.1
/usr/share/man/man1/mesonintrospect.1
/usr/share/man/man1/mesontest.1
/usr/share/man/man1/wraptool.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
