#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-builtins
Version  : 1.4.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/8e/dd/9b7a1d5e8b455c5029998ae6ad2fba1351b71e635b9cac2f4d86cb2ab629/flake8-builtins-1.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/dd/9b7a1d5e8b455c5029998ae6ad2fba1351b71e635b9cac2f4d86cb2ab629/flake8-builtins-1.4.1.tar.gz
Summary  : Check for python builtins being used as variables or parameters.
Group    : Development/Tools
License  : GPL-2.0
Requires: flake8-builtins-license = %{version}-%{release}
Requires: flake8-builtins-python = %{version}-%{release}
Requires: flake8-builtins-python3 = %{version}-%{release}
Requires: configparser
Requires: flake8
Requires: mccabe
Requires: pycodestyle
Requires: pyflakes
BuildRequires : buildreq-distutils3
BuildRequires : configparser
BuildRequires : flake8
BuildRequires : mccabe
BuildRequires : pycodestyle
BuildRequires : pyflakes
BuildRequires : pytest
BuildRequires : python-mock
Patch1: 0001-Fix-test-decorators-to-skip-Python-2-tests.patch

%description
.. image:: https://travis-ci.org/gforcada/flake8-builtins.svg?branch=master
:target: https://travis-ci.org/gforcada/flake8-builtins

%package license
Summary: license components for the flake8-builtins package.
Group: Default

%description license
license components for the flake8-builtins package.


%package python
Summary: python components for the flake8-builtins package.
Group: Default
Requires: flake8-builtins-python3 = %{version}-%{release}

%description python
python components for the flake8-builtins package.


%package python3
Summary: python3 components for the flake8-builtins package.
Group: Default
Requires: python3-core

%description python3
python3 components for the flake8-builtins package.


%prep
%setup -q -n flake8-builtins-1.4.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571078813
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flake8-builtins
cp %{_builddir}/flake8-builtins-1.4.1/LICENSE %{buildroot}/usr/share/package-licenses/flake8-builtins/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/flake8-builtins-1.4.1/LICENSE.rst %{buildroot}/usr/share/package-licenses/flake8-builtins/24aaedad9f47fbf82c0663cc08a429e0d1a99251
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flake8-builtins/24aaedad9f47fbf82c0663cc08a429e0d1a99251
/usr/share/package-licenses/flake8-builtins/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
