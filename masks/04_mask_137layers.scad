// 137-Layer LaH₁₀ Lithography Mask
// For electron beam lithography or focused ion beam

// Parameters
layers = 137;              // The magic number
layer_thickness = 3.68;    // Angstroms
substrate_size = 10000;    // 10 microns
hole_diameter = 50;        // nm
hole_spacing = 100;        // nm

// Golden ratio for hole pattern
phi = (1 + sqrt(5)) / 2;

// Main mask pattern
difference() {
    // Base plate
    cube([substrate_size, substrate_size, 0.1]);
    
    // 137 layers of holes in golden spiral
    for (layer = [0:layers-1]) {
        angle = layer * 360 / phi;
        radius = hole_spacing * sqrt(layer);
        x = radius * cos(angle) + substrate_size/2;
        y = radius * sin(angle) + substrate_size/2;
        
        translate([x, y, -0.1])
            cylinder(h=0.3, d=hole_diameter, $fn=32);
    }
}

// Alignment marks at corners
for (i = [0:3]) {
    rotate([0, 0, 90*i])
        translate([substrate_size*0.45, substrate_size*0.45, 0])
            difference() {
                cube([200, 200, 0.1], center=true);
                cube([100, 100, 0.3], center=true);
            }
}

// Label
translate([100, 100, 0.05])
    linear_extrude(0.05)
        text("137-SC", size=50);
