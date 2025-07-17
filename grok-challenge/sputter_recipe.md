// 137-layer MBE mask
layers=137; pitch=2.46;
for(i=[0:layers-1])
  translate([0,0,i*pitch])
    square([10,1],center=true);
