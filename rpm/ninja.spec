Name:           ninja
Version:        1.12.1
Release:        1
Summary:        Small build system with a focus on speed
License:        ASL 2.0
Url:            https://ninja-build.org/
Source0:        %{name}-%{version}.tar.bz2
Source1:        macros.ninja
Patch1:         0001-Disable-tests-that-fail-with-qemu-JB-44353.patch
BuildRequires:  gcc-c++
BuildRequires:  python3-base
BuildRequires:  re2c >= 0.11.3
BuildRequires:  libstdc++-devel

%description
Ninja is a small build system with a focus on speed. It differs from other
build systems in two major respects: it is designed to have its input files
generated by a higher-level build system, and it is designed to run builds as
fast as possible.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
export CFLAGS="%{optflags}"
%if "%__isa_bits" == "32"
CFLAGS="$CFLAGS -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"
%endif
export CXXFLAGS="%{optflags}"
python3 ./configure.py --bootstrap --verbose

%install
install -D -p -m 0755 ninja %{buildroot}%{_bindir}/ninja
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.ninja

%files
%license COPYING
%{_bindir}/ninja
%{_rpmmacrodir}/macros.ninja
