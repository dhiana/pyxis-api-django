require 'spec_helper'

describe process("gunicorn") do
  it { should be_running }
end
