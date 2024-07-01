#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Roman
Version  : 1.24
Release  : 26
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Roman-1.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Roman-1.24.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/libroman-perl/libroman-perl_1.24-1.debian.tar.xz
Summary  : functions for converting between Roman and Arabic numerals
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Roman-license = %{version}-%{release}
Requires: perl-Roman-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Roman.pm version 1.23
NAME
Roman - Perl module for conversion between Roman and Arabic
numerals.

%package dev
Summary: dev components for the perl-Roman package.
Group: Development
Provides: perl-Roman-devel = %{version}-%{release}
Requires: perl-Roman = %{version}-%{release}

%description dev
dev components for the perl-Roman package.


%package license
Summary: license components for the perl-Roman package.
Group: Default

%description license
license components for the perl-Roman package.


%package perl
Summary: perl components for the perl-Roman package.
Group: Default
Requires: perl-Roman = %{version}-%{release}

%description perl
perl components for the perl-Roman package.


%prep
%setup -q -n Roman-1.24
cd %{_builddir}
tar xf %{_sourcedir}/libroman-perl_1.24-1.debian.tar.xz
cd %{_builddir}/Roman-1.24
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Roman-1.24/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Roman
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Roman/29d093e430a80739858ff0691542788cabff5d4d
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Roman.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Roman/29d093e430a80739858ff0691542788cabff5d4d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
