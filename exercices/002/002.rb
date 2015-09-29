#! /usr/bin/ruby

puts(('a'..'z').to_a.join.reverse.gsub(/a/, 'A').gsub(/e/, 'E').gsub(/i/, 'I').gsub(/o/, 'O').gsub(/u/, 'U'))
