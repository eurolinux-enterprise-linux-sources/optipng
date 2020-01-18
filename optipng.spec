Name:           optipng
Version:        0.7.4
Release:        4%{?dist}
Summary:        PNG optimizer and converter

Group:          Applications/Multimedia
License:        zlib
URL:            http://optipng.sourceforge.net/
Source0:        http://downloads.sourceforge.net/optipng/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  zlib-devel libpng-devel

%description
OptiPNG is a PNG optimizer that recompresses image files to a smaller size,
without losing any information. This program also converts external formats
(BMP, GIF, PNM and TIFF) to optimized PNG, and performs PNG integrity checks
and corrections.


%prep
%setup -q
f=AUTHORS.txt ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f

# Ensure system libs and headers are used; as of 0.6.3 pngxtern will use
# the bundled headers if present even with -with-system-*, causing failures.
rm -rf src/libpng src/zlib


%build
./configure -prefix=%{_prefix} -mandir=%{_mandir} \
    -with-system-zlib -with-system-libpng
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
chmod -c 755 $RPM_BUILD_ROOT%{_bindir}/optipng


%check
make test CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS.txt README.txt LICENSE.txt doc/*
%{_bindir}/optipng
%{_mandir}/man1/optipng.1*


%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.7.4-4
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.7.4-3
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.7.4-1
- Update to 0.7.4.

* Mon Sep 17 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.7.3-1
- Update to 0.7.3.

* Sat Aug 25 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.7.2-1
- Update to 0.7.2.
- Build unit test code with $RPM_(OPT|LD)_FLAGS.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 24 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.7.1-1
- Update to 0.7.1.

* Fri Mar  2 2012 Ville Skyttä <ville.skytta@iki.fi> - 0.7-1
- Update to 0.7.
- Build with $RPM_LD_FLAGS.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.6.5-2
- Rebuild for new libpng

* Thu Apr 28 2011 Ville Skyttä <ville.skytta@iki.fi> - 0.6.5-1
- Update to 0.6.5.
- Patch to fix setjmp.h duplicate inclusion with system libpng.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 15 2010 Till Maas <opensource@till.name> - 0.6.4-1
- update to new release

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 19 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.6.3-1
- Update to 0.6.3.
- Use %%global instead of %%define.

* Wed Feb 25 2009 Till Maas <opensource@till.name> - 0.6.2.1-1
- Update to new release to fix array overflow
- Red Hat Bugzilla #487364

* Wed Nov 12 2008 Till Maas <opensource@till.name> - 0.6.2-1
- Update to new release to fix buffer overflow
- Red Hat Bugzilla #471206

* Thu Aug 28 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-1
- 0.6.1.

* Thu Feb 14 2008 Ville Skyttä <ville.skytta@iki.fi> - 0.5.5-4
- Apply sf.net patch #1790969 to fix crash with -log.
- Cosmetic specfile changes.

* Thu Aug 02 2007 Till Maas <opensource till name> - 0.5.5-3
- update License: Tag according to new Guidelines

* Wed Feb 14 2007 Till Maas <opensource till name> - 0.5.5-2
- rebuild because of new libpng

* Tue Feb 06 2007 Till Maas <opensource till name> - 0.5.5-1
- Version bump

* Wed Nov 29 2006 Till Maas <opensource till name> - 0.5.4-4
- splitting makefile patches
- make LDFLAGS=$RPM_OPT_FLAGS
- Use own makefile define
- Fixing 216784 with upstream patch

* Wed Oct 11 2006 Till Maas <opensource till name> - 0.5.4-3
- bumping release because of errors while importing to extras

* Tue Oct 10 2006 Till Maas <opensource till name> - 0.5.4-2
- shortening Summary

* Thu Sep 14 2006 Till Maas <opensource till name> - 0.5.4-1
- version bump
- use system zlib and libpng
- link without "-s" flag for non-empty debuginfo
- use DESTDIR

* Fri Jul 28 2006 Till Maas <opensource till name> - 0.5.3-1
- version bump
- Changed license tag back to zlib/libpng (#198616 rpmlint) 
- use $RPM_OPT_FLAGS instead of %%{optflags}

* Thu Jul 06 2006 Till Maas <opensource till name> - 0.5.2-2
- Changed license tag from zlib/libpng to zlib

* Tue Jul 04 2006 Till Maas <opensource till name> - 0.5.2-1
- Created from scratch for fedora extras
