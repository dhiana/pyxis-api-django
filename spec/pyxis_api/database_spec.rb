require 'spec_helper'

describe 'required database configs' do
  describe file('/home/vagrant/pyxis-api-django/pyxis_api/pyxis_api/settings.py') do
    it { should exist }
    its(:content) { should match /^.*'HOST'.*192\.168\.33\.42.*$/ }
  end
end
