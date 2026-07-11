%global tl_name babel-czech
%global tl_revision 30261

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1a
Release:	%{tl_revision}.1
Summary:	Babel support for Czech
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/czech
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-czech.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-czech.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-czech.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of Czech
in babel. Some shortcuts are defined, as well as translations to Czech
of standard "LaTeX names".

