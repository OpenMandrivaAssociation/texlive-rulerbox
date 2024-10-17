Name:		texlive-rulerbox
Version:	50984
Release:	2
Summary:	Draw rulers around a box
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rulerbox
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rulerbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rulerbox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package for drawing rulers around a box. This
might be useful when showing the absolute size of something in
electronic documents, or designating the relative scale in
printed materials.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/rulerbox
%doc %{_texmfdistdir}/doc/latex/rulerbox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
