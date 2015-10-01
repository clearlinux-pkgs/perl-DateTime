#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime
Version  : 1.21
Release  : 3
URL      : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-1.21.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/DateTime-1.21.tar.gz
Summary  : 'A date and time object for Perl'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-DateTime-lib
Requires: perl-DateTime-doc
BuildRequires : perl(DateTime::Locale)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(Module::Build)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Try::Tiny)

%description
NAME
DateTime - A date and time object for Perl
VERSION
version 1.21
SYNOPSIS
use DateTime;

$dt = DateTime->new(
year       => 1964,
month      => 10,
day        => 16,
hour       => 16,
minute     => 12,
second     => 47,
nanosecond => 500000000,
time_zone  => 'Asia/Taipei',
);

$dt = DateTime->from_epoch( epoch => $epoch );
$dt = DateTime->now; # same as ( epoch => time() )

$year   = $dt->year;
$month  = $dt->month;          # 1-12

$day    = $dt->day;            # 1-31

$dow    = $dt->day_of_week;    # 1-7 (Monday is 1)

$hour   = $dt->hour;           # 0-23
$minute = $dt->minute;         # 0-59

$second = $dt->second;         # 0-61 (leap seconds!)

$doy    = $dt->day_of_year;    # 1-366 (leap years)

$doq    = $dt->day_of_quarter; # 1..

$qtr    = $dt->quarter;        # 1-4

# all of the start-at-1 methods above have corresponding start-at-0
# methods, such as $dt->day_of_month_0, $dt->month_0 and so on

$ymd    = $dt->ymd;           # 2002-12-06
$ymd    = $dt->ymd('/');      # 2002/12/06

$mdy    = $dt->mdy;           # 12-06-2002
$mdy    = $dt->mdy('/');      # 12/06/2002

$dmy    = $dt->dmy;           # 06-12-2002
$dmy    = $dt->dmy('/');      # 06/12/2002

$hms    = $dt->hms;           # 14:02:29
$hms    = $dt->hms('!');      # 14!02!29

$is_leap  = $dt->is_leap_year;

# these are localizable, see Locales section
$month_name  = $dt->month_name; # January, February, ...
$month_abbr  = $dt->month_abbr; # Jan, Feb, ...
$day_name    = $dt->day_name;   # Monday, Tuesday, ...
$day_abbr    = $dt->day_abbr;   # Mon, Tue, ...

# May not work for all possible datetime, see the docs on this
# method for more details.
$epoch_time  = $dt->epoch;

$dt2 = $dt + $duration_object;

$dt3 = $dt - $duration_object;

$duration_object = $dt - $dt2;

$dt->set( year => 1882 );

$dt->set_time_zone( 'America/Chicago' );

$dt->set_formatter( $formatter );

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
%setup -q -n DateTime-1.21

%build
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
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/DateTime.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/DateTime/Duration.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/DateTime/Helpers.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/DateTime/Infinite.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/DateTime/LeapSecond.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/DateTime/PP.pm
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/DateTime/PPExtra.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.22.0/x86_64-linux/auto/DateTime/DateTime.so
