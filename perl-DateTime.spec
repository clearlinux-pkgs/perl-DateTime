#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime
Version  : 1.44
Release  : 20
URL      : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-1.44.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-1.44.tar.gz
Summary  : 'A date and time object for Perl'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-DateTime-lib
Requires: perl-DateTime-doc
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(CPAN::Meta::Check)
BuildRequires : perl(Class::Singleton)
BuildRequires : perl(DateTime::Locale)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(Dist::CheckConflicts)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Specio)
BuildRequires : perl(Specio::Declare)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Specio::Library::Builtins)
BuildRequires : perl(Specio::Library::Numeric)
BuildRequires : perl(Specio::Library::String)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
# NAME
DateTime - A date and time object for Perl
# VERSION
version 1.44
# SYNOPSIS

%package doc
Summary: doc components for the perl-DateTime package.
Group: Documentation

%description doc
doc components for the perl-DateTime package.


%package lib
Summary: lib components for the perl-DateTime package.
Group: Libraries

%description lib
lib components for the perl-DateTime package.


%prep
%setup -q -n DateTime-1.44

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DateTime.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DateTime/Conflicts.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DateTime/Duration.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DateTime/Helpers.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DateTime/Infinite.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DateTime/LeapSecond.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DateTime/PP.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DateTime/PPExtra.pm
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/DateTime/Types.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.0/x86_64-linux-thread-multi/auto/DateTime/DateTime.so
