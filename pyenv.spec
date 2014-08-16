Name: pyenv
Version: 20140705
Release: 1%{?dist}
BuildArch: noarch
Summary: A simple Python version manager
License: MIT
URL: https://github.com/yyuu/%{name}
Requires: bash

# URL: https://github.com/yyuu/%{name}/archive/v%{version}.tar.gz
Source0: %{name}-%{version}.tar.gz
Patch0: 0001-Include-usr-share-pyenv-in-plugin-search-path.patch

%description
Pyenv lets you easily switch between multiple versions of Python. It
is simple, unobtrusive, and follows the UNIX tradition of
single-purpose tools that do one thing well. The features of pyenv
include: letting you change the global Python version on a per-user
basis, providing support for per-project Python versions, allowing you
to override the Python version with an environment variable, and
searching commands from multiple versions of Python at a time.

%prep
%setup
%patch0 -p1

%install
mkdir -p %{buildroot}/usr/libexec
for f in libexec/*; do
    install "$f" %{buildroot}/usr/libexec
done

BIN_DIR=%{buildroot}/usr/bin
mkdir -p ${BIN_DIR}
cp -P bin/pyenv ${BIN_DIR}
install bin/python-local-exec %{buildroot}/usr/bin

PLUGIN_DIR=%{buildroot}/usr/share/pyenv/plugins/python-build
mkdir -p ${PLUGIN_DIR}
cp -r plugins/python-build/bin ${PLUGIN_DIR}
cp -r plugins/python-build/share ${PLUGIN_DIR}

%files
%doc CHANGELOG.md
%doc COMMANDS.md
%doc LICENSE
%doc README.md
/usr/bin/*
/usr/libexec/*
%dir /usr/share/pyenv/plugins

%package python-build
Summary: A pyenv plugin for installing Python versions
Requires: %{name} = %{version}-%{release}
Requires: bash
Requires: gcc-c++
Requires: readline-devel
Requires: zlib-devel
Requires: bzip2-devel
Requires: openssl-devel
Requires: sqlite-devel

%description python-build
The python-build plugin for pyenv provides a `pyenv install` command
to compile and install different versions of Python on UNIX-like
systems.

%files python-build
%doc plugins/python-build/README.md
/usr/share/pyenv/plugins/python-build/bin
/usr/share/pyenv/plugins/python-build/share