%global srcname dulwich
%global sum A python implementation of the Git file formats and protocols

%filter_provides_in %{python2_sitearch}
%filter_provides_in %{python3_sitearch}
%filter_setup

Name:           python-%{srcname}
Version:        0.11.2
Release:        3%{?dist}
Summary:        %{sum}

License:        GPLv2+ or ASL 2.0
URL:            http://samba.org/~jelmer/dulwich/
Source0:        https://pypi.python.org/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz

BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python2-nose
BuildRequires:  python2-nose
BuildRequires:  python-sphinx
BuildRequires:  python-docutils
BuildRequires:  python3-sphinx
BuildRequires:  python3-docutils

%if 0%{?rhel} < 7 || 0%{?fedora} < 14
BuildRequires:  python-unittest2
%endif

%description
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Dulwich is a pure-Python implementation of the Git file formats and
protocols. The project is named after the village in which Mr. and
Mrs. Git live in the Monty Python sketch.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
pushd docs
# Not using {smp_flags} as sphinx fails with it from time to time
make html
popd
%py3_build
pushd docs
# Not using {smp_flags} as sphinx fails with it from time to time
make html
popd

%install
%py2_install
# Remove extra copy of text docs
rm -rf docs/build/html/_sources
rm -f docs/build/html/{.buildinfo,objects.inv}
rm -rf %{buildroot}%{python2_sitearch}/docs/tutorial/
%py3_install
# Remove extra copy of text docs
rm -rf docs/build/html/_sources
rm -f docs/build/html/{.buildinfo,objects.inv}
rm -rf %{buildroot}%{python3_sitearch}/docs/tutorial/

#%check
#cd dulwich/tests
#nosetests test*.py

%files -n python2-%{srcname}
%doc AUTHORS docs/build/html
%license COPYING
%{_bindir}/dul-*
%{_bindir}/%{srcname}
%{python2_sitearch}/%{srcname}*
%exclude %{python2_sitearch}/%{srcname}/tests*

%files -n python3-%{srcname}
%doc AUTHORS docs/build/html
%license COPYING
%{_bindir}/dul-*
%{_bindir}/%{srcname}
%{python3_sitearch}/%{srcname}*
%exclude %{python3_sitearch}/%{srcname}/tests*

%changelog
* Sat Nov 14 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.2-3
- Cleanup and py3

* Tue Oct 06 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.2-2
- Update docs
- Update to new upstream version 0.11.2

* Tue Oct 06 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.1-1
- Update to new upstream version 0.11.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.0-1
- Fix for CVE-2014-9706 (rhbz#1204889, rhbz#1204890, and rhbz#1204891)
- Update to new upstream version 0.10.0

* Mon Mar 23 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.9-1
- Update to new upstream version 0.9.9

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.7-1
- Update to new upstream version 0.9.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.6-1
- Update to new upstream version 0.9.6

* Wed Feb 26 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.5-1
- Tests are currently not working
- Update to new upstream version 0.9.5

* Mon Oct 28 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Update to new upstream version 0.9.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to new upstream version 0.9.0
- Now dual-licensed GPLv2+ or ASL 2.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.7-1
- Update to new upstream version 0.8.7

* Sat Nov 10 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.6-1
- Update to new upstream version 0.8.6

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 23 2012 Matěj Cepl <mcepl@redhat.com> - 0.8.5-2
- We don’t need python-unittest2 anymore.

* Fri Apr 13 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.5-1
- Update to new upstream version 0.8.5

* Fri Apr 06 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.4-1
- Update to new upstream version 0.8.4

* Fri Feb 24 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.3-1
- Update to new upstream version 0.8.3

* Sat Jan 28 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-2
- Add missing BR

* Fri Jan 27 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.2-1
- Update to new upstream version 0.8.2

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.0-1
- Update to new upstream version 0.8.0

* Sun Apr 17 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.1-1
- Update to new upstream version 0.7.1

* Fri Mar 11 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-3
- Test section reworked

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.7.0-1
- Update to new upstream version 0.7.0

* Mon Nov 08 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.2-1
- Filtering added
- Update to new upstream version 0.6.2

* Wed Sep 01 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.1-1
- Fix grep parameter
- Run all test now
- Update to new upstream version 0.6.1

* Sat Jul 03 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-3
- Remove exec permission from test.py
- Add python-nose

* Fri Jun 25 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-2
- Change summary
- Change to srcname
- Fix rpmlint issue
- Add check section and exclude the tests directory

* Thu Jun 17 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Fix some rpmlint issues
- Add docs directory
- Update to new upstream version 0.6.0

* Wed Apr 28 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-2
- Add Doc
- Add BR setuptools

* Fri Apr 16 2010 Steve 'Ashcrow' Milner <me@stevemilner.org> 0.5.0-1
- Initial package
