%define module UPS-Nut
%define pmodule UPS/Nut

Summary: A  perl module to talk to a UPS via NUT upsd
Name:    perl-%module
Version: 0.04
Release: 7
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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.04-6mdv2010.0
+ Revision: 430611
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.04-5mdv2009.0
+ Revision: 242120
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.04-3mdv2008.0
+ Revision: 23625
- rebuild


* Mon Jun 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-2mdk
- rebuild for new Perl

* Fri Nov 07 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-1mdk
- initial release

