Name: pyenv-virtualenv
Version: 1.0.0
Release: 1%{?dist}
BuildArch: noarch
Summary: A pyenv plugin to manage virtualenv environments
License: MIT
URL: https://github.com/yyuu/%{name}
Requires: pyenv >= 1.0.0
Requires: bash

Source0: https://github.com/yyuu/%{name}/archive/v%{version}.tar.gz

%description

The pyenv-virtualenv plugin for pyenv provides a `pyenv virtualenv`
command to create pyenv-compataible virtualenv environments for Python
on UNIX-like systems.

%prep
%setup

%install
PLUGIN_DIR=%{buildroot}/usr/share/pyenv/plugins/%{name}
mkdir -p ${PLUGIN_DIR}
cp -r bin ${PLUGIN_DIR}

%files
%doc LICENSE
%doc README.md
/usr/share/pyenv/plugins/%{name}
