require 'spec_helper'

describe 'requiriments check' do


  describe command('python -c "import django"') do
    its(:exit_status) { should eq 0 }
  end
end
