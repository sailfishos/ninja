Name:           ninja
Version:        1.8.2
Release:        0
Summary:        A small build system closest in spirit to Make
License:        ASL 2.0
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

rm misc/zsh-completion
rm misc/ninja.vim
rm misc/bash-completion

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/rpm/macros.ninja

%check
./ninja ninja_test
./ninja_test

%files
%doc COPYING
%{_bindir}/ninja
%{_sysconfdir}/rpm/macros.ninja

