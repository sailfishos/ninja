#
# spec file for package ninja
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ninja
Version:        1.8.2
Release:        0
Summary:        A small build system closest in spirit to Make
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://ninja-build.org/
Source0:        https://github.com/ninja-build/ninja/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        macros.ninja
BuildRequires:  gcc-c++
BuildRequires:  python3-base
BuildRequires:  re2c

%description
Ninja is yet another build system. It takes as input the interdependencies
of files (typically source code and output executables) and orchestrates
building them, quickly.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
python3 ./configure.py --bootstrap --verbose

%install
install -D -p -m 0755 ninja %{buildroot}%{_bindir}/ninja
install -D -p -m 0644 misc/zsh-completion %{buildroot}%{_datadir}/zsh/site-functions/_ninja
install -D -p -m 0644 misc/ninja.vim %{buildroot}%{_datadir}/vim/site/syntax/ninja.vim
install -D -p -m 0644 misc/bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/ninja
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.ninja

%check
./ninja ninja_test
./ninja_test

%files
%doc COPYING
%{_bindir}/ninja
%{_datadir}/zsh
%{_datadir}/vim
%{_sysconfdir}/bash_completion.d
%{_rpmconfigdir}/macros.d/macros.ninja

%changelog

