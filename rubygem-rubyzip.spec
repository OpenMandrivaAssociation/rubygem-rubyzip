%define oname rubyzip

Name:       rubygem-%{oname}
Version:    0.9.4
Release:    %mkrel 2
Summary:    A ruby module for reading and writing zip files
Group:      Development/Ruby
License:    GPLv2+ or Ruby License
URL:        http://rubyzip.sourceforge.net/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
rubyzip is a ruby module for reading and writing zip files


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/samples/ -type f \
  -name "*.rb" -exec chmod 755 {} \;
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test/ -type f \
  -name "*.rb" -exec chmod 755 {} \;
chmod 755 %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/install.rb
chmod 644 %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
for f in `find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib/ -type f` ; do
    sed -i -e '/^#!/d' $f
    chmod 644 $f
done

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/install.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/samples/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/ChangeLog
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/NEWS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/TODO
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
