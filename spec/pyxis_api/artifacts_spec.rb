require 'spec_helper'

describe 'required artifacts' do
  describe file('/home/vagrant/pyxis-api-django') do
    it { should exist }
    it { should be_directory }
  end
end
