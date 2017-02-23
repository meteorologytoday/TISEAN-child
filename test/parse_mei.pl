#!/bin/perl
use strict;

print "#year month_cnt val\n";
while(<>) {
	if (/(\d{4})(\s+[\-\d.]+)+\n/) {
		my @a = split(/\s+/, $_);
		my $y = shift(@a);
		my $m = 0;
		foreach my $val (@a) {
			print "$y $m $val\n";
			++$m;
		}
	}
}
