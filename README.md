# Block model: Ionic conduction model for macroscopic powder compacts of Li-ion solid electrolytes. 
**The "blockwalk.py" and "blockwalk2.py" were developed for simulating ion conduction of solid electrolyte compacts.** These programs simulate how a ion moves within a block-type percolation model and calculate the curvature of its pathway. I anticipate that this program could be applied not only to ion conductors but also to various conduction models in other fields.  

## Background
The article for the research using this program was published in the [following paper](https://doi.org/10.2109/jcersj2.24062).

**Li-ion conductors are expected to be applied as solid electrolytes in all-solid-state batteries.** Compared to conventional Li-ion batteries, all-solid-state batteries offer higher safety and energy density, making them promising for applications such as electric vehicles. Enhancing the ion conductivity of solid electrolytes is essential for improving the performance of all-solid-state batteries. 

**In this paper, I have developed a macroscopic compact-scale ionic conduction model,** as opposed to the commonly performed evaluation of ion conduction performance at the crystal structure scale.  

It has been reported that there is a power-law relationship between the packing density and the conductivity of powder compacts. For the representative Li-based solid electrolyte, Li₃PS₄ glass, I confirmed through both experiments and simulations that the conductivity scales as the packing density raised to the power of 1.8.  

At present, the placement of voids is entirely random. However, to enable application to more complex systems, I am considering developing programs that account for biased distributions of voids in the future.  
