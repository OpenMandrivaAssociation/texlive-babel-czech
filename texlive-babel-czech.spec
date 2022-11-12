Name:		texlive-babel-czech
Version:	30261
Release:	1
Summary:	TeXLive babel-czech package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-czech.r30261.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-czech.doc.r30261.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-czech.source.r30261.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-czech package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-czech/czech.ldf
%doc %{_texmfdistdir}/doc/generic/babel-czech/czech.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-czech/czech.dtx
%doc %{_texmfdistdir}/source/generic/babel-czech/czech.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
