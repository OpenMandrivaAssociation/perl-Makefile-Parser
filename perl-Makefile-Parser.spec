%define upstream_name    Makefile-Parser
%define upstream_version 0.211

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    GNU makefile parser using GNU make's database dump
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Makefile/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Trigger)
BuildRequires: perl(Cwd)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IPC::Run3)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(List::Util)
BuildRequires: perl(Makefile::DOM)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Balanced)
BuildRequires: perl(Time::HiRes)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
The structure of this (GNU) makefile AST is designed based on GNU make's
data base listing output produced by '--print-data-base'.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm t/makesimple.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes META.yml
%{_bindir}/makesimple
%{_bindir}/pgmake-db
%{_bindir}/plmake
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*


