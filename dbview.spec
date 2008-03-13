Summary:	dbview - view dBase files
Summary(pl.UTF-8):	Program do oglądania plików dBase
Name:		dbview
Version:	1.0.4
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/database/proprietary/%{name}-%{version}.tar.gz
# Source0-md5:	aba3a1137b17cf4915641612fb200562
Patch0:		%{name}-make.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbview is a little tool that will display dBase III and IV files. You
can also use it to convert your old .dbf files for further use with
Unix.

%description -l pl.UTF-8
dbview jest małym programem wyświetlającym zawartość plików dBase III
i IV. Można go wykorzystać do konwersji starych plików .dbf do
wykorzystania pod Uniksem.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README dBASE
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
