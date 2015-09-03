require 'spec_helper'

describe 'required packages' do
  @packages = ['mysql-client',
               'python-pip',
               'python-dev',
               'libmysqlclient-dev',
               'git']

  @packages.each do |package|
    describe package(package) do
      it { should be_installed }
    end
  end
end
