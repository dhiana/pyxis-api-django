require 'spec_helper'

describe package('mysql-client') do
  it { should be_installed }
end
