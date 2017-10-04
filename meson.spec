#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : meson
Version  : 0.42.1
Release  : 6
URL      : https://github.com/mesonbuild/meson/releases/download/0.42.1/meson-0.42.1.tar.gz
Source0  : https://github.com/mesonbuild/meson/releases/download/0.42.1/meson-0.42.1.tar.gz
Summary  : A high performance build system
Group    : Development/Tools
License  : Apache-2.0
Requires: meson-bin
Requires: meson-python3
Requires: meson-doc
Requires: meson-python
Requires: ninja
BuildRequires : cmake
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : setuptools

%description
fast and as user friendly as possible. It supports many languages and compilers, including
        GCC, Clang and Visual Studio. Its build definitions are written in a simple non-turing
        complete DSL.

%package bin
Summary: bin components for the meson package.
Group: Binaries

%description bin
bin components for the meson package.


%package doc
Summary: doc components for the meson package.
Group: Documentation

%description doc
doc components for the meson package.


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
%setup -q -n meson-0.42.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507158555
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

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
