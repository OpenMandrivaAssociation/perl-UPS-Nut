%define module UPS-Nut
%define pmodule UPS/Nut

Summary: A  perl module to talk to a UPS via NUT upsd
Name:    perl-%module
Version: 0.04
Release: 2mdk
License: GPL or Artistic
Group:   Monitoring
Source:  %module-%version.tar.bz2
BuildRequires: perl-devel
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is an object-oriented interface between Perl and upsd (Network UPS
Tools package).

%prep
%setup -q -n %module-%version


%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os -s"
perl Makefile.PL INSTALLDIRS=vendor
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc Changes LICENSE README
%{_mandir}/*/*
%{perl_vendorlib}/UPS/Nut.pm

