%global tl_name rulerbox
%global tl_revision 50984

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Draw rulers around a box
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rulerbox
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rulerbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rulerbox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX package for drawing rulers around a box. This might be
useful when showing the absolute size of something in electronic
documents, or designating the relative scale in printed materials.

