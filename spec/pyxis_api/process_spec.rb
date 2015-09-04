require 'spec_helper'

describe process("gunicorn") do
  it { should be_running }
end

describe port(5000) do
  it { should be_listening }
end
