Summary:	dbview - view dBase files
Summary(pl):	Program do ogl±dania plików dBase
Name:		dbview
Version:	1.0.3
Release:	4
License:	GPL
Group:		Applications/Databases
Group(de):	Applikationen/Dateibanken
Group(pl):	Aplikacje/Bazy danych
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/database/proprietary/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-fixes.patch
Icon:		dbview.xpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbview is a little tool that will display dBase III and IV files. You
can also use it to convert your old .dbf files for further use with
Unix.

%description -l pl
dbview jest ma³ym programem wy¶wietlaj±cym zawarto¶æ plików dBase III
i IV. Mo¿na go wykorzystaæ do konwersji starych plików .dbf do
wykorzystania pod Uniksem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README dBASE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
