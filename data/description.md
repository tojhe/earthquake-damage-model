# Problem description
We're trying to predict the [ordinal variable](https://www.ma.utexas.edu/users/mks/statmistakes/ordinal.html) `damage_grade`, which represents a level of damage to the building that was hit by the earthquake. There are 3 grades of the damage:

  * `1` represents low damage
  * `2` represents a medium amount of damage
  * `3` represents almost complete destruction

    <b>Features</b>
    <br>[List of features](#Features)
    <br>[Example of features](Feature_data_example)

    <br><b>Performance metric</b>
                <li><a href="#metric">Example</a></li>
            </ul>
        </div>
        <div>
            <ul style="list-style: none">
                <li><strong>Submission Format</strong></li>
                <li><a href="#submission-format">Format example</a></li>
            </ul>
        </div>
    </div>
</div>

<a name="Features"></a>
## Features
<hr>
<p>The dataset mainly consists of information on the buildings' structure and their legal ownership. Each row in the dataset represents a specific building in the region that was hit by Gorkha earthquake.</p>
<p>There are 39 columns in this dataset, where the <code>building_id</code> column is a unique and random identifier. The remaining 38 features are described in the section below. Categorical variables have been obfuscated random lowercase ascii characters. The appearance of the same character in distinct columns does <strong>not</strong> imply the same original value.</p>

## Description
<ul>
<li><code>geo_level_1_id</code>, <code>geo_level_2_id</code>, <code>geo_level_3_id</code> (type: int): geographic region in which building exists, from largest (level 1) to most specific sub-region (level 3). Possible values: level 1: 0-30, level 2: 0-1427, level 3: 0-12567.</li>
<li><code>count_floors_pre_eq</code> (type: int): number of floors in the building before the earthquake.</li>
<li><code>age</code> (type: int): age of the building in years.</li>
<li><code>area_percentage</code> (type: int): normalized area of the building footprint.</li>
<li><code>height_percentage</code> (type: int): normalized height of the building footprint.</li>
<li><code>land_surface_condition</code> (type: categorical): surface condition of the land where the building was built. Possible values: n, o, t.</li>
<li><code>foundation_type</code> (type: categorical): type of foundation used while building. Possible values: h, i, r, u, w.</li>
<li><code>roof_type</code> (type: categorical): type of roof used while building. Possible values: n, q, x.</li>
<li><code>ground_floor_type</code> (type: categorical): type of the ground floor. Possible values: f, m, v, x, z.</li>
<li><code>other_floor_type</code> (type: categorical): type of constructions used in higher than the ground floors (except of roof). Possible values: j, q, s, x.</li>
<li><code>position</code> (type: categorical): position of the building. Possible values: j, o, s, t.</li>
<li><code>plan_configuration</code> (type: categorical): building plan configuration. Possible values: a, c, d, f, m, n, o, q, s, u.</li>
<li><code>has_superstructure_adobe_mud</code> (type: binary): flag variable that indicates if the superstructure was made of Adobe/Mud.</li>
<li><code>has_superstructure_mud_mortar_stone</code> (type: binary): flag variable that indicates if the superstructure was made of Mud Mortar - Stone.</li>
<li><code>has_superstructure_stone_flag</code> (type: binary): flag variable that indicates if the superstructure was made of Stone.</li>
<li><code>has_superstructure_cement_mortar_stone</code> (type: binary): flag variable that indicates if the superstructure was made of Cement Mortar - Stone.</li>
<li><code>has_superstructure_mud_mortar_brick</code> (type: binary): flag variable that indicates if the superstructure was made of Mud Mortar - Brick.</li>
<li><code>has_superstructure_cement_mortar_brick</code> (type: binary): flag variable that indicates if the superstructure was made of Cement Mortar - Brick.</li>
<li><code>has_superstructure_timber</code> (type: binary): flag variable that indicates if the superstructure was made of Timber.</li>
<li><code>has_superstructure_bamboo</code> (type: binary): flag variable that indicates if the superstructure was made of Bamboo.</li>
<li><code>has_superstructure_rc_non_engineered</code> (type: binary): flag variable that indicates if the superstructure was made of non-engineered reinforced concrete.</li>
<li><code>has_superstructure_rc_engineered</code> (type: binary): flag variable that indicates if the superstructure was made of engineered reinforced concrete.</li>
<li><code>has_superstructure_other</code> (type: binary): flag variable that indicates if the superstructure was made of any other material.</li>
<li><code>legal_ownership_status</code> (type: categorical): legal ownership status of the land where building was built. Possible values: a, r, v, w.</li>
<li><code>count_families</code>  (type: int): number of families that live in the building.</li>
<li><code>has_secondary_use</code> (type: binary): flag variable that indicates if the building was used for any secondary purpose.</li>
<li><code>has_secondary_use_agriculture</code> (type: binary): flag variable that indicates if the building was used for agricultural purposes.</li>
<li><code>has_secondary_use_hotel</code> (type: binary): flag variable that indicates if the building was used as a hotel.</li>
<li><code>has_secondary_use_rental</code> (type: binary): flag variable that indicates if the building was used for rental purposes.</li>
<li><code>has_secondary_use_institution</code> (type: binary): flag variable that indicates if the building was used as a location of any institution.</li>
<li><code>has_secondary_use_school</code> (type: binary): flag variable that indicates if the building was used as a school.</li>
<li><code>has_secondary_use_industry</code> (type: binary): flag variable that indicates if the building was used for industrial purposes.</li>
<li><code>has_secondary_use_health_post</code> (type: binary): flag variable that indicates if the building was used as a health post.</li>
<li><code>has_secondary_use_gov_office</code> (type: binary): flag variable that indicates if the building was used fas a government office.</li>
<li><code>has_secondary_use_use_police</code> (type: binary): flag variable that indicates if the building was used as a police station.</li>
<li><code>has_secondary_use_other</code> (type: binary): flag variable that indicates if the building was secondarily used for other purposes.</li>
</ul>

<div>

### Feature data example

<hr>

Here's an example of one of the rows in the dataset so that you can see the kinds of values you might expect in the dataset. Some are numeric, some are categorical, and there are often missing values.

<br>
<br>

<table style="width:70%; margin-left:15%; margin-right:15%;" class="table">
<thead>
<tr class="header">
<th>field</th>
<th>value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>geo_level_1_id</td>
<td>8</td>
</tr>
<tr class="even">
<td>geo_level_2_id</td>
<td>396</td>
</tr>
<tr class="odd">
<td>geo_level_3_id</td>
<td>1108</td>
</tr>
<tr class="even">
<td>count_floors_pre_eq</td>
<td>2</td>
</tr>
<tr class="odd">
<td>age</td>
<td>15</td>
</tr>
<tr class="even">
<td>area_percentage</td>
<td>4</td>
</tr>
<tr class="odd">
<td>height_percentage</td>
<td>7</td>
</tr>
<tr class="even">
<td>land_surface_condition</td>
<td>t</td>
</tr>
<tr class="odd">
<td>foundation_type</td>
<td>r</td>
</tr>
<tr class="even">
<td>roof_type</td>
<td>n</td>
</tr>
<tr class="odd">
<td>ground_floor_type</td>
<td>v</td>
</tr>
<tr class="even">
<td>other_floor_type</td>
<td>q</td>
</tr>
<tr class="odd">
<td>position</td>
<td>s</td>
</tr>
<tr class="even">
<td>plan_configuration</td>
<td>d</td>
</tr>
<tr class="odd">
<td>has_superstructure_adobe_mud</td>
<td>1</td>
</tr>
<tr class="even">
<td>has_superstructure_mud_mortar_stone</td>
<td>1</td>
</tr>
<tr class="odd">
<td>has_superstructure_stone_flag</td>
<td>0</td>
</tr>
<tr class="even">
<td>has_superstructure_cement_mortar_stone</td>
<td>0</td>
</tr>
<tr class="odd">
<td>has_superstructure_mud_mortar_brick</td>
<td>0</td>
</tr>
<tr class="even">
<td>has_superstructure_cement_mortar_brick</td>
<td>1</td>
</tr>
<tr class="odd">
<td>has_superstructure_timber</td>
<td>0</td>
</tr>
<tr class="even">
<td>has_superstructure_bamboo</td>
<td>0</td>
</tr>
<tr class="odd">
<td>has_superstructure_rc_non_engineered</td>
<td>0</td>
</tr>
<tr class="even">
<td>has_superstructure_rc_engineered</td>
<td>0</td>
</tr>
<tr class="odd">
<td>has_superstructure_other</td>
<td>1</td>
</tr>
<tr class="even">
<td>legal_ownership_status</td>
<td>v</td>
</tr>
<tr class="odd">
<td>count_families</td>
<td>1</td>
</tr>
<tr class="even">
<td>has_secondary_use</td>
<td>0</td>
</tr>
<tr class="odd">
<td>has_secondary_use_agriculture</td>
<td>0</td>
</tr>
<tr class="even">
<td>has_secondary_use_hotel</td>
<td>0</td>
</tr>
<tr class="odd">
<td>has_secondary_use_rental</td>
<td>0</td>
</tr>
<tr class="even">
<td>has_secondary_use_institution</td>
<td>0</td>
</tr>
<tr class="odd">
<td>has_secondary_use_school</td>
<td>0</td>
</tr>
<tr class="even">
<td>has_secondary_use_industry</td>
<td>0</td>
</tr>
<tr class="odd">
<td>has_secondary_use_health_post</td>
<td>0</td>
</tr>
<tr class="even">
<td>has_secondary_use_gov_office</td>
<td>0</td>
</tr>
<tr class="odd">
<td>has_secondary_use_use_police</td>
<td>0</td>
</tr>
<tr class="even">
<td>has_secondary_use_other</td>
<td>0</td>
</tr>
</tbody>
</table>

</div>

<p><a id="metric" target="_blank"></a></p>
<h2>Performance metric</h2>
<hr>
<p>We are predicting the level of damage from 1 to 3. The level of damage is an ordinal variable meaning that ordering is important. This can be viewed as a <em>classification</em> or an <em>ordinal regression</em> problem. (Ordinal regression is sometimes described as an problem somewhere in between classification and regression.)</p>
<p>To measure the performance of our algorithms, we'll use the <strong>F1 score</strong> which balances the <a href="https://en.wikipedia.org/wiki/Precision_and_recall" target="_blank">precision and recall</a> of a classifier. Traditionally, the F1 score is used to evaluate performance on a binary classifier, but since we have three possible labels we will use a variant called the <strong>micro averaged F1 score</strong>.</p>
<p><span class="MathJax_Preview" style="color: inherit; display: none;"></span><div class="MathJax_Display" style="text-align: center;"><span class="MathJax" id="MathJax-Element-1-Frame" tabindex="0" style="text-align: center; position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot; display=&quot;block&quot;><msub><mi>F</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mo>&amp;#x22C5;</mo><msub><mi>P</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>&amp;#x22C5;</mo><msub><mi>R</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub></mrow><mrow><msub><mi>P</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>+</mo><msub><mi>R</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub></mrow></mfrac></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-1" style="width: 14.089em; display: inline-block;"><span style="display: inline-block; position: relative; width: 11.347em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(0.863em, 1011.35em, 3.39em, -999.997em); top: -2.363em; left: 0em;"><span class="mrow" id="MathJax-Span-2"><span class="msubsup" id="MathJax-Span-3"><span style="display: inline-block; position: relative; width: 2.53em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-4" style="font-family: MathJax_Math-italic;">F<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.648em;"><span class="texatom" id="MathJax-Span-5"><span class="mrow" id="MathJax-Span-6"><span class="mi" id="MathJax-Span-7" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-8" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-9" style="font-size: 70.7%; font-family: MathJax_Math-italic;">c</span><span class="mi" id="MathJax-Span-10" style="font-size: 70.7%; font-family: MathJax_Math-italic;">r</span><span class="mi" id="MathJax-Span-11" style="font-size: 70.7%; font-family: MathJax_Math-italic;">o</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-12" style="font-family: MathJax_Main; padding-left: 0.272em;">=</span><span class="mfrac" id="MathJax-Span-13" style="padding-left: 0.272em;"><span style="display: inline-block; position: relative; width: 7.261em; height: 0px; margin-right: 0.11em; margin-left: 0.11em;"><span style="position: absolute; clip: rect(3.121em, 1007.15em, 4.304em, -999.997em); top: -4.675em; left: 50%; margin-left: -3.546em;"><span class="mrow" id="MathJax-Span-14"><span class="mn" id="MathJax-Span-15" style="font-family: MathJax_Main;">2</span><span class="mo" id="MathJax-Span-16" style="font-family: MathJax_Main; padding-left: 0.218em;">⋅</span><span class="msubsup" id="MathJax-Span-17" style="padding-left: 0.218em;"><span style="display: inline-block; position: relative; width: 2.53em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-18" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.648em;"><span class="texatom" id="MathJax-Span-19"><span class="mrow" id="MathJax-Span-20"><span class="mi" id="MathJax-Span-21" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-22" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-23" style="font-size: 70.7%; font-family: MathJax_Math-italic;">c</span><span class="mi" id="MathJax-Span-24" style="font-size: 70.7%; font-family: MathJax_Math-italic;">r</span><span class="mi" id="MathJax-Span-25" style="font-size: 70.7%; font-family: MathJax_Math-italic;">o</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-26" style="font-family: MathJax_Main; padding-left: 0.218em;">⋅</span><span class="msubsup" id="MathJax-Span-27" style="padding-left: 0.218em;"><span style="display: inline-block; position: relative; width: 2.691em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-28" style="font-family: MathJax_Math-italic;">R</span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.755em;"><span class="texatom" id="MathJax-Span-29"><span class="mrow" id="MathJax-Span-30"><span class="mi" id="MathJax-Span-31" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-32" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-33" style="font-size: 70.7%; font-family: MathJax_Math-italic;">c</span><span class="mi" id="MathJax-Span-34" style="font-size: 70.7%; font-family: MathJax_Math-italic;">r</span><span class="mi" id="MathJax-Span-35" style="font-size: 70.7%; font-family: MathJax_Math-italic;">o</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(3.121em, 1006.45em, 4.304em, -999.997em); top: -3.277em; left: 50%; margin-left: -3.223em;"><span class="mrow" id="MathJax-Span-36"><span class="msubsup" id="MathJax-Span-37"><span style="display: inline-block; position: relative; width: 2.53em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-38" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.648em;"><span class="texatom" id="MathJax-Span-39"><span class="mrow" id="MathJax-Span-40"><span class="mi" id="MathJax-Span-41" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-42" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-43" style="font-size: 70.7%; font-family: MathJax_Math-italic;">c</span><span class="mi" id="MathJax-Span-44" style="font-size: 70.7%; font-family: MathJax_Math-italic;">r</span><span class="mi" id="MathJax-Span-45" style="font-size: 70.7%; font-family: MathJax_Math-italic;">o</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-46" style="font-family: MathJax_Main; padding-left: 0.218em;">+</span><span class="msubsup" id="MathJax-Span-47" style="padding-left: 0.218em;"><span style="display: inline-block; position: relative; width: 2.691em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-48" style="font-family: MathJax_Math-italic;">R</span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.755em;"><span class="texatom" id="MathJax-Span-49"><span class="mrow" id="MathJax-Span-50"><span class="mi" id="MathJax-Span-51" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-52" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-53" style="font-size: 70.7%; font-family: MathJax_Math-italic;">c</span><span class="mi" id="MathJax-Span-54" style="font-size: 70.7%; font-family: MathJax_Math-italic;">r</span><span class="mi" id="MathJax-Span-55" style="font-size: 70.7%; font-family: MathJax_Math-italic;">o</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(0.863em, 1007.26em, 1.239em, -999.997em); top: -1.288em; left: 0em;"><span style="display: inline-block; overflow: hidden; vertical-align: 0em; border-top: 1.3px solid; width: 7.261em; height: 0px;"></span><span style="display: inline-block; width: 0px; height: 1.078em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.368em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -1.13em; border-left: 0px solid; width: 0px; height: 2.87em;"></span></span></nobr><span class="MJX_Assistive_MathML MJX_Assistive_MathML_Block" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>F</mi><mrow class="MJX-TeXAtom-ORD"><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>=</mo><mfrac><mrow><mn>2</mn><mo>⋅</mo><msub><mi>P</mi><mrow class="MJX-TeXAtom-ORD"><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>⋅</mo><msub><mi>R</mi><mrow class="MJX-TeXAtom-ORD"><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub></mrow><mrow><msub><mi>P</mi><mrow class="MJX-TeXAtom-ORD"><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>+</mo><msub><mi>R</mi><mrow class="MJX-TeXAtom-ORD"><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub></mrow></mfrac></math></span></span></div><script type="math/tex; mode=display" id="MathJax-Element-1">F_{micro} = \frac{2 \cdot P_{micro} \cdot R_{micro}}{P_{micro} + R_{micro}}</script></p>
<p>where</p>
<p><span class="MathJax_Preview" style="color: inherit; display: none;"></span><div class="MathJax_Display" style="text-align: center;"><span class="MathJax" id="MathJax-Element-2-Frame" tabindex="0" style="text-align: center; position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot; display=&quot;block&quot;><msub><mi>P</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>=</mo><mfrac><mrow><munderover><mo>&amp;#x2211;</mo><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mn>3</mn></mrow></munderover><mi>T</mi><msub><mi>P</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi></mrow></msub></mrow><mrow><munderover><mo>&amp;#x2211;</mo><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mn>3</mn></mrow></munderover><mo stretchy=&quot;false&quot;>(</mo><mi>T</mi><msub><mi>P</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi></mrow></msub><mo>+</mo><mi>F</mi><msub><mi>P</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi></mrow></msub><mo stretchy=&quot;false&quot;>)</mo></mrow></mfrac><mo>,</mo><mtext>&amp;#xA0;</mtext><mtext>&amp;#xA0;</mtext><msub><mi>R</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>=</mo><mfrac><mrow><munderover><mo>&amp;#x2211;</mo><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mn>3</mn></mrow></munderover><mi>T</mi><msub><mi>P</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi></mrow></msub></mrow><mrow><munderover><mo>&amp;#x2211;</mo><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mn>3</mn></mrow></munderover><mo stretchy=&quot;false&quot;>(</mo><mi>T</mi><msub><mi>P</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi></mrow></msub><mo>+</mo><mi>F</mi><msub><mi>N</mi><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mi>k</mi></mrow></msub><mo stretchy=&quot;false&quot;>)</mo></mrow></mfrac></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-56" style="width: 31.831em; display: inline-block;"><span style="display: inline-block; position: relative; width: 25.648em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(0.487em, 1025.65em, 3.766em, -999.997em); top: -2.363em; left: 0em;"><span class="mrow" id="MathJax-Span-57"><span class="msubsup" id="MathJax-Span-58"><span style="display: inline-block; position: relative; width: 2.53em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-59" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.648em;"><span class="texatom" id="MathJax-Span-60"><span class="mrow" id="MathJax-Span-61"><span class="mi" id="MathJax-Span-62" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-63" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-64" style="font-size: 70.7%; font-family: MathJax_Math-italic;">c</span><span class="mi" id="MathJax-Span-65" style="font-size: 70.7%; font-family: MathJax_Math-italic;">r</span><span class="mi" id="MathJax-Span-66" style="font-size: 70.7%; font-family: MathJax_Math-italic;">o</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-67" style="font-family: MathJax_Main; padding-left: 0.272em;">=</span><span class="mfrac" id="MathJax-Span-68" style="padding-left: 0.272em;"><span style="display: inline-block; position: relative; width: 8.121em; height: 0px; margin-right: 0.11em; margin-left: 0.11em;"><span style="position: absolute; clip: rect(2.852em, 1004.36em, 4.411em, -999.997em); top: -4.728em; left: 50%; margin-left: -2.202em;"><span class="mrow" id="MathJax-Span-69"><span class="munderover" id="MathJax-Span-70"><span style="display: inline-block; position: relative; width: 2.422em; height: 0px;"><span style="position: absolute; clip: rect(3.067em, 1001.02em, 4.411em, -999.997em); top: -3.976em; left: 0em;"><span class="mo" id="MathJax-Span-71" style="font-family: MathJax_Size1; vertical-align: 0em;">∑</span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1000.43em, 4.142em, -999.997em); top: -4.46em; left: 1.078em;"><span class="texatom" id="MathJax-Span-72"><span class="mrow" id="MathJax-Span-73"><span class="mn" id="MathJax-Span-74" style="font-size: 70.7%; font-family: MathJax_Main;">3</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1001.35em, 4.142em, -999.997em); top: -3.707em; left: 1.078em;"><span class="texatom" id="MathJax-Span-75"><span class="mrow" id="MathJax-Span-76"><span class="mi" id="MathJax-Span-77" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span class="mo" id="MathJax-Span-78" style="font-size: 70.7%; font-family: MathJax_Main;">=</span><span class="mn" id="MathJax-Span-79" style="font-size: 70.7%; font-family: MathJax_Main;">1</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mi" id="MathJax-Span-80" style="font-family: MathJax_Math-italic; padding-left: 0.164em;">T<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span class="msubsup" id="MathJax-Span-81"><span style="display: inline-block; position: relative; width: 1.078em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-82" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.648em;"><span class="texatom" id="MathJax-Span-83"><span class="mrow" id="MathJax-Span-84"><span class="mi" id="MathJax-Span-85" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(2.852em, 1007.91em, 4.411em, -999.997em); top: -3.062em; left: 50%; margin-left: -4.03em;"><span class="mrow" id="MathJax-Span-86"><span class="munderover" id="MathJax-Span-87"><span style="display: inline-block; position: relative; width: 2.422em; height: 0px;"><span style="position: absolute; clip: rect(3.067em, 1001.02em, 4.411em, -999.997em); top: -3.976em; left: 0em;"><span class="mo" id="MathJax-Span-88" style="font-family: MathJax_Size1; vertical-align: 0em;">∑</span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1000.43em, 4.142em, -999.997em); top: -4.46em; left: 1.078em;"><span class="texatom" id="MathJax-Span-89"><span class="mrow" id="MathJax-Span-90"><span class="mn" id="MathJax-Span-91" style="font-size: 70.7%; font-family: MathJax_Main;">3</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1001.35em, 4.142em, -999.997em); top: -3.707em; left: 1.078em;"><span class="texatom" id="MathJax-Span-92"><span class="mrow" id="MathJax-Span-93"><span class="mi" id="MathJax-Span-94" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span class="mo" id="MathJax-Span-95" style="font-size: 70.7%; font-family: MathJax_Main;">=</span><span class="mn" id="MathJax-Span-96" style="font-size: 70.7%; font-family: MathJax_Main;">1</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-97" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-98" style="font-family: MathJax_Math-italic;">T<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span class="msubsup" id="MathJax-Span-99"><span style="display: inline-block; position: relative; width: 1.078em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-100" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.648em;"><span class="texatom" id="MathJax-Span-101"><span class="mrow" id="MathJax-Span-102"><span class="mi" id="MathJax-Span-103" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-104" style="font-family: MathJax_Main; padding-left: 0.218em;">+</span><span class="mi" id="MathJax-Span-105" style="font-family: MathJax_Math-italic; padding-left: 0.218em;">F<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span class="msubsup" id="MathJax-Span-106"><span style="display: inline-block; position: relative; width: 1.078em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-107" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.648em;"><span class="texatom" id="MathJax-Span-108"><span class="mrow" id="MathJax-Span-109"><span class="mi" id="MathJax-Span-110" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-111" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(0.863em, 1008.12em, 1.239em, -999.997em); top: -1.288em; left: 0em;"><span style="display: inline-block; overflow: hidden; vertical-align: 0em; border-top: 1.3px solid; width: 8.121em; height: 0px;"></span><span style="display: inline-block; width: 0px; height: 1.078em;"></span></span></span></span><span class="mo" id="MathJax-Span-112" style="font-family: MathJax_Main;">,</span><span class="mtext" id="MathJax-Span-113" style="font-family: MathJax_Main; padding-left: 0.164em;">&nbsp;</span><span class="mtext" id="MathJax-Span-114" style="font-family: MathJax_Main;">&nbsp;</span><span class="msubsup" id="MathJax-Span-115"><span style="display: inline-block; position: relative; width: 2.691em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-116" style="font-family: MathJax_Math-italic;">R</span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.755em;"><span class="texatom" id="MathJax-Span-117"><span class="mrow" id="MathJax-Span-118"><span class="mi" id="MathJax-Span-119" style="font-size: 70.7%; font-family: MathJax_Math-italic;">m</span><span class="mi" id="MathJax-Span-120" style="font-size: 70.7%; font-family: MathJax_Math-italic;">i</span><span class="mi" id="MathJax-Span-121" style="font-size: 70.7%; font-family: MathJax_Math-italic;">c</span><span class="mi" id="MathJax-Span-122" style="font-size: 70.7%; font-family: MathJax_Math-italic;">r</span><span class="mi" id="MathJax-Span-123" style="font-size: 70.7%; font-family: MathJax_Math-italic;">o</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-124" style="font-family: MathJax_Main; padding-left: 0.272em;">=</span><span class="mfrac" id="MathJax-Span-125" style="padding-left: 0.272em;"><span style="display: inline-block; position: relative; width: 8.282em; height: 0px; margin-right: 0.11em; margin-left: 0.11em;"><span style="position: absolute; clip: rect(2.852em, 1004.36em, 4.411em, -999.997em); top: -4.728em; left: 50%; margin-left: -2.202em;"><span class="mrow" id="MathJax-Span-126"><span class="munderover" id="MathJax-Span-127"><span style="display: inline-block; position: relative; width: 2.422em; height: 0px;"><span style="position: absolute; clip: rect(3.067em, 1001.02em, 4.411em, -999.997em); top: -3.976em; left: 0em;"><span class="mo" id="MathJax-Span-128" style="font-family: MathJax_Size1; vertical-align: 0em;">∑</span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1000.43em, 4.142em, -999.997em); top: -4.46em; left: 1.078em;"><span class="texatom" id="MathJax-Span-129"><span class="mrow" id="MathJax-Span-130"><span class="mn" id="MathJax-Span-131" style="font-size: 70.7%; font-family: MathJax_Main;">3</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1001.35em, 4.142em, -999.997em); top: -3.707em; left: 1.078em;"><span class="texatom" id="MathJax-Span-132"><span class="mrow" id="MathJax-Span-133"><span class="mi" id="MathJax-Span-134" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span class="mo" id="MathJax-Span-135" style="font-size: 70.7%; font-family: MathJax_Main;">=</span><span class="mn" id="MathJax-Span-136" style="font-size: 70.7%; font-family: MathJax_Main;">1</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mi" id="MathJax-Span-137" style="font-family: MathJax_Math-italic; padding-left: 0.164em;">T<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span class="msubsup" id="MathJax-Span-138"><span style="display: inline-block; position: relative; width: 1.078em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-139" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.648em;"><span class="texatom" id="MathJax-Span-140"><span class="mrow" id="MathJax-Span-141"><span class="mi" id="MathJax-Span-142" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(2.852em, 1008.07em, 4.411em, -999.997em); top: -3.062em; left: 50%; margin-left: -4.083em;"><span class="mrow" id="MathJax-Span-143"><span class="munderover" id="MathJax-Span-144"><span style="display: inline-block; position: relative; width: 2.422em; height: 0px;"><span style="position: absolute; clip: rect(3.067em, 1001.02em, 4.411em, -999.997em); top: -3.976em; left: 0em;"><span class="mo" id="MathJax-Span-145" style="font-family: MathJax_Size1; vertical-align: 0em;">∑</span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1000.43em, 4.142em, -999.997em); top: -4.46em; left: 1.078em;"><span class="texatom" id="MathJax-Span-146"><span class="mrow" id="MathJax-Span-147"><span class="mn" id="MathJax-Span-148" style="font-size: 70.7%; font-family: MathJax_Main;">3</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(3.336em, 1001.35em, 4.142em, -999.997em); top: -3.707em; left: 1.078em;"><span class="texatom" id="MathJax-Span-149"><span class="mrow" id="MathJax-Span-150"><span class="mi" id="MathJax-Span-151" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span><span class="mo" id="MathJax-Span-152" style="font-size: 70.7%; font-family: MathJax_Main;">=</span><span class="mn" id="MathJax-Span-153" style="font-size: 70.7%; font-family: MathJax_Main;">1</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-154" style="font-family: MathJax_Main;">(</span><span class="mi" id="MathJax-Span-155" style="font-family: MathJax_Math-italic;">T<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span class="msubsup" id="MathJax-Span-156"><span style="display: inline-block; position: relative; width: 1.078em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.75em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-157" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.648em;"><span class="texatom" id="MathJax-Span-158"><span class="mrow" id="MathJax-Span-159"><span class="mi" id="MathJax-Span-160" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-161" style="font-family: MathJax_Main; padding-left: 0.218em;">+</span><span class="mi" id="MathJax-Span-162" style="font-family: MathJax_Math-italic; padding-left: 0.218em;">F<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span class="msubsup" id="MathJax-Span-163"><span style="display: inline-block; position: relative; width: 1.239em; height: 0px;"><span style="position: absolute; clip: rect(3.121em, 1000.92em, 4.142em, -999.997em); top: -3.976em; left: 0em;"><span class="mi" id="MathJax-Span-164" style="font-family: MathJax_Math-italic;">N<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; top: -3.815em; left: 0.809em;"><span class="texatom" id="MathJax-Span-165"><span class="mrow" id="MathJax-Span-166"><span class="mi" id="MathJax-Span-167" style="font-size: 70.7%; font-family: MathJax_Math-italic;">k</span></span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span></span></span><span class="mo" id="MathJax-Span-168" style="font-family: MathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 3.981em;"></span></span><span style="position: absolute; clip: rect(0.863em, 1008.28em, 1.239em, -999.997em); top: -1.288em; left: 0em;"><span style="display: inline-block; overflow: hidden; vertical-align: 0em; border-top: 1.3px solid; width: 8.282em; height: 0px;"></span><span style="display: inline-block; width: 0px; height: 1.078em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.368em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -1.597em; border-left: 0px solid; width: 0px; height: 3.737em;"></span></span></nobr><span class="MJX_Assistive_MathML MJX_Assistive_MathML_Block" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>P</mi><mrow class="MJX-TeXAtom-ORD"><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>=</mo><mfrac><mrow><munderover><mo>∑</mo><mrow class="MJX-TeXAtom-ORD"><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow class="MJX-TeXAtom-ORD"><mn>3</mn></mrow></munderover><mi>T</mi><msub><mi>P</mi><mrow class="MJX-TeXAtom-ORD"><mi>k</mi></mrow></msub></mrow><mrow><munderover><mo>∑</mo><mrow class="MJX-TeXAtom-ORD"><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow class="MJX-TeXAtom-ORD"><mn>3</mn></mrow></munderover><mo stretchy="false">(</mo><mi>T</mi><msub><mi>P</mi><mrow class="MJX-TeXAtom-ORD"><mi>k</mi></mrow></msub><mo>+</mo><mi>F</mi><msub><mi>P</mi><mrow class="MJX-TeXAtom-ORD"><mi>k</mi></mrow></msub><mo stretchy="false">)</mo></mrow></mfrac><mo>,</mo><mtext>&nbsp;</mtext><mtext>&nbsp;</mtext><msub><mi>R</mi><mrow class="MJX-TeXAtom-ORD"><mi>m</mi><mi>i</mi><mi>c</mi><mi>r</mi><mi>o</mi></mrow></msub><mo>=</mo><mfrac><mrow><munderover><mo>∑</mo><mrow class="MJX-TeXAtom-ORD"><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow class="MJX-TeXAtom-ORD"><mn>3</mn></mrow></munderover><mi>T</mi><msub><mi>P</mi><mrow class="MJX-TeXAtom-ORD"><mi>k</mi></mrow></msub></mrow><mrow><munderover><mo>∑</mo><mrow class="MJX-TeXAtom-ORD"><mi>k</mi><mo>=</mo><mn>1</mn></mrow><mrow class="MJX-TeXAtom-ORD"><mn>3</mn></mrow></munderover><mo stretchy="false">(</mo><mi>T</mi><msub><mi>P</mi><mrow class="MJX-TeXAtom-ORD"><mi>k</mi></mrow></msub><mo>+</mo><mi>F</mi><msub><mi>N</mi><mrow class="MJX-TeXAtom-ORD"><mi>k</mi></mrow></msub><mo stretchy="false">)</mo></mrow></mfrac></math></span></span></div><script type="math/tex; mode=display" id="MathJax-Element-2">P_{micro} = \frac{\sum_{k=1}^{3}TP_{k}}{\sum_{k=1}^{3}(TP_{k} + FP_{k})},~~R_{micro} = \frac{\sum_{k=1}^{3}TP_{k}}{\sum_{k=1}^{3}(TP_{k} + FN_{k})}</script></p>
<p>and <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-3-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>T</mi><mi>P</mi></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-169" style="width: 1.831em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.454em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.508em, 1001.45em, 2.53em, -999.997em); top: -2.363em; left: 0em;"><span class="mrow" id="MathJax-Span-170"><span class="mi" id="MathJax-Span-171" style="font-family: MathJax_Math-italic;">T<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span class="mi" id="MathJax-Span-172" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.368em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.063em; border-left: 0px solid; width: 0px; height: 1.003em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>T</mi><mi>P</mi></math></span></span><script type="math/tex" id="MathJax-Element-3">TP</script> is True Positive, <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-4-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>F</mi><mi>P</mi></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-173" style="width: 1.884em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.508em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.508em, 1001.51em, 2.53em, -999.997em); top: -2.363em; left: 0em;"><span class="mrow" id="MathJax-Span-174"><span class="mi" id="MathJax-Span-175" style="font-family: MathJax_Math-italic;">F<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span class="mi" id="MathJax-Span-176" style="font-family: MathJax_Math-italic;">P<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.368em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.063em; border-left: 0px solid; width: 0px; height: 1.003em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mi>P</mi></math></span></span><script type="math/tex" id="MathJax-Element-4">FP</script> is False Positive, <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-5-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>F</mi><mi>N</mi></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-177" style="width: 2.099em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.669em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.508em, 1001.67em, 2.53em, -999.997em); top: -2.363em; left: 0em;"><span class="mrow" id="MathJax-Span-178"><span class="mi" id="MathJax-Span-179" style="font-family: MathJax_Math-italic;">F<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span><span class="mi" id="MathJax-Span-180" style="font-family: MathJax_Math-italic;">N<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.11em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.368em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.063em; border-left: 0px solid; width: 0px; height: 1.003em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>F</mi><mi>N</mi></math></span></span><script type="math/tex" id="MathJax-Element-5">FN</script> is False Negative, and <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-6-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>k</mi></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-181" style="width: 0.702em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.54em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.508em, 1000.54em, 2.53em, -999.997em); top: -2.363em; left: 0em;"><span class="mrow" id="MathJax-Span-182"><span class="mi" id="MathJax-Span-183" style="font-family: MathJax_Math-italic;">k</span></span><span style="display: inline-block; width: 0px; height: 2.368em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.063em; border-left: 0px solid; width: 0px; height: 1.003em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>k</mi></math></span></span><script type="math/tex" id="MathJax-Element-6">k</script> represents each class in <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-7-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-184" style="width: 2.96em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.368em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.562em, 1002.32em, 2.745em, -999.997em); top: -2.363em; left: 0em;"><span class="mrow" id="MathJax-Span-185"><span class="texatom" id="MathJax-Span-186"><span class="mrow" id="MathJax-Span-187"><span class="mn" id="MathJax-Span-188" style="font-family: MathJax_Main;">1</span><span class="mo" id="MathJax-Span-189" style="font-family: MathJax_Main;">,</span><span class="mn" id="MathJax-Span-190" style="font-family: MathJax_Main; padding-left: 0.164em;">2</span><span class="mo" id="MathJax-Span-191" style="font-family: MathJax_Main;">,</span><span class="mn" id="MathJax-Span-192" style="font-family: MathJax_Main; padding-left: 0.164em;">3</span></span></span></span><span style="display: inline-block; width: 0px; height: 2.368em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.33em; border-left: 0px solid; width: 0px; height: 1.203em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow class="MJX-TeXAtom-ORD"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></math></span></span><script type="math/tex" id="MathJax-Element-7">{1,2,3}</script>.</p>
<p>In Python, you can easily calculate this loss using <code>sklearn.metrics.f1_score</code> with the keyword argument <code>average='micro'</code>. Here are some references that discuss the micro-averaged F1 score further:</p>
<ul>
<li><a href="http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html" target="_blank"> Scikit-Learn Documentation</a></li>
<li><a href="http://rushdishams.blogspot.com/2011/08/micro-and-macro-average-of-precision.html" target="_blank">Blog Post</a></li>
</ul>
<p><a id="submission-format" target="_blank"></a></p>
<h2>Submission format</h2>
<hr>
<p>The format for the submission file is two columns with the <code>building_id</code> and the <code>damage_grade</code>. The data type of <code>damage_grade</code> is an integer with values of <span class="MathJax_Preview" style="color: inherit; display: none;"></span><span class="MathJax" id="MathJax-Element-8-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mrow class=&quot;MJX-TeXAtom-ORD&quot;><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-193" style="width: 2.96em; display: inline-block;"><span style="display: inline-block; position: relative; width: 2.368em; height: 0px; font-size: 124%;"><span style="position: absolute; clip: rect(1.562em, 1002.32em, 2.745em, -999.997em); top: -2.363em; left: 0em;"><span class="mrow" id="MathJax-Span-194"><span class="texatom" id="MathJax-Span-195"><span class="mrow" id="MathJax-Span-196"><span class="mn" id="MathJax-Span-197" style="font-family: MathJax_Main;">1</span><span class="mo" id="MathJax-Span-198" style="font-family: MathJax_Main;">,</span><span class="mn" id="MathJax-Span-199" style="font-family: MathJax_Main; padding-left: 0.164em;">2</span><span class="mo" id="MathJax-Span-200" style="font-family: MathJax_Main;">,</span><span class="mn" id="MathJax-Span-201" style="font-family: MathJax_Main; padding-left: 0.164em;">3</span></span></span></span><span style="display: inline-block; width: 0px; height: 2.368em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.33em; border-left: 0px solid; width: 0px; height: 1.203em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mrow class="MJX-TeXAtom-ORD"><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mn>3</mn></mrow></math></span></span><script type="math/tex" id="MathJax-Element-8">{1, 2, 3}</script>, <strong>so make sure there is no decimal point and no other numbers in your submission</strong>. For example <code>1</code> would be valid, and <code>1.0</code> would <strong>not</strong>.</p>
<p>For example, if you predicted:</p>
<table class="table table-striped">
<thead>
<tr class="header">
<th>building_id</th>
<th>damage_grade</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11456</td>
<td>1</td>
</tr>
<tr class="even">
<td>16528</td>
<td>1</td>
</tr>
<tr class="odd">
<td>3253</td>
<td>1</td>
</tr>
<tr class="even">
<td>18614</td>
<td>1</td>
</tr>
<tr class="odd">
<td>1544</td>
<td>1</td>
</tr>
</tbody>
</table>

<p>The first few lines of the <code>.csv</code> file that you submit would look like:</p>
<pre><code>building_id,damage_grade
11456,1
16528,1
3253,1
18614,1
1544,1
</code></pre>
<h2>Good luck!</h2>
<hr>
<p>Good luck and enjoy this problem! If you have any questions you can always visit the <a href="http://community.drivendata.org/">user forum</a>!</p>

        </div>
