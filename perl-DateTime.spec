#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime
Version  : 1.55
Release  : 58
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-1.55.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-1.55.tar.gz
Summary  : 'A date and time object for Perl'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-DateTime-perl = %{version}-%{release}
Requires: perl(DateTime::Locale)
Requires: perl(DateTime::TimeZone)
Requires: perl(Dist::CheckConflicts)
BuildRequires : buildreq-cpan
BuildRequires : perl(CPAN::Meta::Check)
BuildRequires : perl(DateTime::Locale)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(Dist::CheckConflicts)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Specio)
BuildRequires : perl(Specio::Declare)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Specio::Library::Builtins)
BuildRequires : perl(Specio::Library::Numeric)
BuildRequires : perl(Specio::Library::String)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(namespace::autoclean)

%description
# NAME
DateTime - A date and time object for Perl
# VERSION
version 1.55
# SYNOPSIS

%package dev
Summary: dev components for the perl-DateTime package.
Group: Development
Provides: perl-DateTime-devel = %{version}-%{release}
Requires: perl-DateTime = %{version}-%{release}

%description dev
dev components for the perl-DateTime package.


%package perl
Summary: perl components for the perl-DateTime package.
Group: Default
Requires: perl-DateTime = %{version}-%{release}

%description perl
perl components for the perl-DateTime package.


%prep
%setup -q -n DateTime-1.55
cd %{_builddir}/DateTime-1.55

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

%install
rm -rf %{buildroot}
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
/usr/share/man/man3/DateTime.3
/usr/share/man/man3/DateTime::Duration.3
/usr/share/man/man3/DateTime::Infinite.3
/usr/share/man/man3/DateTime::LeapSecond.3
/usr/share/man/man3/DateTime::Types.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DateTime.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DateTime/Conflicts.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DateTime/Duration.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DateTime/Helpers.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DateTime/Infinite.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DateTime/LeapSecond.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DateTime/PP.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DateTime/PPExtra.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/DateTime/Types.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/DateTime/DateTime.so
