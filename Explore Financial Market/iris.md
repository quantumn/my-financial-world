

```R
 library(dplyr)
```

    
    Attaching package: 'dplyr'
    
    The following object is masked from 'package:stats':
    
        filter
    
    The following objects are masked from 'package:base':
    
        intersect, setdiff, setequal, union
    
    


```R
iris

```




<table>
<thead><tr><th></th><th scope=col>Sepal.Length</th><th scope=col>Sepal.Width</th><th scope=col>Petal.Length</th><th scope=col>Petal.Width</th><th scope=col>Species</th></tr></thead>
<tbody>
	<tr><th scope=row>1</th><td>5.1</td><td>3.5</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>2</th><td>4.9</td><td>3</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>3</th><td>4.7</td><td>3.2</td><td>1.3</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>4</th><td>4.6</td><td>3.1</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>5</th><td>5</td><td>3.6</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>6</th><td>5.4</td><td>3.9</td><td>1.7</td><td>0.4</td><td>setosa</td></tr>
	<tr><th scope=row>7</th><td>4.6</td><td>3.4</td><td>1.4</td><td>0.3</td><td>setosa</td></tr>
	<tr><th scope=row>8</th><td>5</td><td>3.4</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>9</th><td>4.4</td><td>2.9</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>10</th><td>4.9</td><td>3.1</td><td>1.5</td><td>0.1</td><td>setosa</td></tr>
	<tr><th scope=row>11</th><td>5.4</td><td>3.7</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>12</th><td>4.8</td><td>3.4</td><td>1.6</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>13</th><td>4.8</td><td>3</td><td>1.4</td><td>0.1</td><td>setosa</td></tr>
	<tr><th scope=row>14</th><td>4.3</td><td>3</td><td>1.1</td><td>0.1</td><td>setosa</td></tr>
	<tr><th scope=row>15</th><td>5.8</td><td>4</td><td>1.2</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>16</th><td>5.7</td><td>4.4</td><td>1.5</td><td>0.4</td><td>setosa</td></tr>
	<tr><th scope=row>17</th><td>5.4</td><td>3.9</td><td>1.3</td><td>0.4</td><td>setosa</td></tr>
	<tr><th scope=row>18</th><td>5.1</td><td>3.5</td><td>1.4</td><td>0.3</td><td>setosa</td></tr>
	<tr><th scope=row>19</th><td>5.7</td><td>3.8</td><td>1.7</td><td>0.3</td><td>setosa</td></tr>
	<tr><th scope=row>20</th><td>5.1</td><td>3.8</td><td>1.5</td><td>0.3</td><td>setosa</td></tr>
	<tr><th scope=row>21</th><td>5.4</td><td>3.4</td><td>1.7</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>22</th><td>5.1</td><td>3.7</td><td>1.5</td><td>0.4</td><td>setosa</td></tr>
	<tr><th scope=row>23</th><td>4.6</td><td>3.6</td><td>1</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>24</th><td>5.1</td><td>3.3</td><td>1.7</td><td>0.5</td><td>setosa</td></tr>
	<tr><th scope=row>25</th><td>4.8</td><td>3.4</td><td>1.9</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>26</th><td>5</td><td>3</td><td>1.6</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>27</th><td>5</td><td>3.4</td><td>1.6</td><td>0.4</td><td>setosa</td></tr>
	<tr><th scope=row>28</th><td>5.2</td><td>3.5</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>29</th><td>5.2</td><td>3.4</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>30</th><td>4.7</td><td>3.2</td><td>1.6</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>31</th><td>4.8</td><td>3.1</td><td>1.6</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>32</th><td>5.4</td><td>3.4</td><td>1.5</td><td>0.4</td><td>setosa</td></tr>
	<tr><th scope=row>33</th><td>5.2</td><td>4.1</td><td>1.5</td><td>0.1</td><td>setosa</td></tr>
	<tr><th scope=row>34</th><td>5.5</td><td>4.2</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>35</th><td>4.9</td><td>3.1</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>36</th><td>5</td><td>3.2</td><td>1.2</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>37</th><td>5.5</td><td>3.5</td><td>1.3</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>38</th><td>4.9</td><td>3.6</td><td>1.4</td><td>0.1</td><td>setosa</td></tr>
	<tr><th scope=row>39</th><td>4.4</td><td>3</td><td>1.3</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>40</th><td>5.1</td><td>3.4</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>41</th><td>5</td><td>3.5</td><td>1.3</td><td>0.3</td><td>setosa</td></tr>
	<tr><th scope=row>42</th><td>4.5</td><td>2.3</td><td>1.3</td><td>0.3</td><td>setosa</td></tr>
	<tr><th scope=row>43</th><td>4.4</td><td>3.2</td><td>1.3</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>44</th><td>5</td><td>3.5</td><td>1.6</td><td>0.6</td><td>setosa</td></tr>
	<tr><th scope=row>45</th><td>5.1</td><td>3.8</td><td>1.9</td><td>0.4</td><td>setosa</td></tr>
	<tr><th scope=row>46</th><td>4.8</td><td>3</td><td>1.4</td><td>0.3</td><td>setosa</td></tr>
	<tr><th scope=row>47</th><td>5.1</td><td>3.8</td><td>1.6</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>48</th><td>4.6</td><td>3.2</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>49</th><td>5.3</td><td>3.7</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>50</th><td>5</td><td>3.3</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>
	<tr><th scope=row>51</th><td>7</td><td>3.2</td><td>4.7</td><td>1.4</td><td>versicolor</td></tr>
	<tr><th scope=row>52</th><td>6.4</td><td>3.2</td><td>4.5</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>53</th><td>6.9</td><td>3.1</td><td>4.9</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>54</th><td>5.5</td><td>2.3</td><td>4</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>55</th><td>6.5</td><td>2.8</td><td>4.6</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>56</th><td>5.7</td><td>2.8</td><td>4.5</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>57</th><td>6.3</td><td>3.3</td><td>4.7</td><td>1.6</td><td>versicolor</td></tr>
	<tr><th scope=row>58</th><td>4.9</td><td>2.4</td><td>3.3</td><td>1</td><td>versicolor</td></tr>
	<tr><th scope=row>59</th><td>6.6</td><td>2.9</td><td>4.6</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>60</th><td>5.2</td><td>2.7</td><td>3.9</td><td>1.4</td><td>versicolor</td></tr>
	<tr><th scope=row>61</th><td>5</td><td>2</td><td>3.5</td><td>1</td><td>versicolor</td></tr>
	<tr><th scope=row>62</th><td>5.9</td><td>3</td><td>4.2</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>63</th><td>6</td><td>2.2</td><td>4</td><td>1</td><td>versicolor</td></tr>
	<tr><th scope=row>64</th><td>6.1</td><td>2.9</td><td>4.7</td><td>1.4</td><td>versicolor</td></tr>
	<tr><th scope=row>65</th><td>5.6</td><td>2.9</td><td>3.6</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>66</th><td>6.7</td><td>3.1</td><td>4.4</td><td>1.4</td><td>versicolor</td></tr>
	<tr><th scope=row>67</th><td>5.6</td><td>3</td><td>4.5</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>68</th><td>5.8</td><td>2.7</td><td>4.1</td><td>1</td><td>versicolor</td></tr>
	<tr><th scope=row>69</th><td>6.2</td><td>2.2</td><td>4.5</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>70</th><td>5.6</td><td>2.5</td><td>3.9</td><td>1.1</td><td>versicolor</td></tr>
	<tr><th scope=row>71</th><td>5.9</td><td>3.2</td><td>4.8</td><td>1.8</td><td>versicolor</td></tr>
	<tr><th scope=row>72</th><td>6.1</td><td>2.8</td><td>4</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>73</th><td>6.3</td><td>2.5</td><td>4.9</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>74</th><td>6.1</td><td>2.8</td><td>4.7</td><td>1.2</td><td>versicolor</td></tr>
	<tr><th scope=row>75</th><td>6.4</td><td>2.9</td><td>4.3</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>76</th><td>6.6</td><td>3</td><td>4.4</td><td>1.4</td><td>versicolor</td></tr>
	<tr><th scope=row>77</th><td>6.8</td><td>2.8</td><td>4.8</td><td>1.4</td><td>versicolor</td></tr>
	<tr><th scope=row>78</th><td>6.7</td><td>3</td><td>5</td><td>1.7</td><td>versicolor</td></tr>
	<tr><th scope=row>79</th><td>6</td><td>2.9</td><td>4.5</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>80</th><td>5.7</td><td>2.6</td><td>3.5</td><td>1</td><td>versicolor</td></tr>
	<tr><th scope=row>81</th><td>5.5</td><td>2.4</td><td>3.8</td><td>1.1</td><td>versicolor</td></tr>
	<tr><th scope=row>82</th><td>5.5</td><td>2.4</td><td>3.7</td><td>1</td><td>versicolor</td></tr>
	<tr><th scope=row>83</th><td>5.8</td><td>2.7</td><td>3.9</td><td>1.2</td><td>versicolor</td></tr>
	<tr><th scope=row>84</th><td>6</td><td>2.7</td><td>5.1</td><td>1.6</td><td>versicolor</td></tr>
	<tr><th scope=row>85</th><td>5.4</td><td>3</td><td>4.5</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>86</th><td>6</td><td>3.4</td><td>4.5</td><td>1.6</td><td>versicolor</td></tr>
	<tr><th scope=row>87</th><td>6.7</td><td>3.1</td><td>4.7</td><td>1.5</td><td>versicolor</td></tr>
	<tr><th scope=row>88</th><td>6.3</td><td>2.3</td><td>4.4</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>89</th><td>5.6</td><td>3</td><td>4.1</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>90</th><td>5.5</td><td>2.5</td><td>4</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>91</th><td>5.5</td><td>2.6</td><td>4.4</td><td>1.2</td><td>versicolor</td></tr>
	<tr><th scope=row>92</th><td>6.1</td><td>3</td><td>4.6</td><td>1.4</td><td>versicolor</td></tr>
	<tr><th scope=row>93</th><td>5.8</td><td>2.6</td><td>4</td><td>1.2</td><td>versicolor</td></tr>
	<tr><th scope=row>94</th><td>5</td><td>2.3</td><td>3.3</td><td>1</td><td>versicolor</td></tr>
	<tr><th scope=row>95</th><td>5.6</td><td>2.7</td><td>4.2</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>96</th><td>5.7</td><td>3</td><td>4.2</td><td>1.2</td><td>versicolor</td></tr>
	<tr><th scope=row>97</th><td>5.7</td><td>2.9</td><td>4.2</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>98</th><td>6.2</td><td>2.9</td><td>4.3</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>99</th><td>5.1</td><td>2.5</td><td>3</td><td>1.1</td><td>versicolor</td></tr>
	<tr><th scope=row>100</th><td>5.7</td><td>2.8</td><td>4.1</td><td>1.3</td><td>versicolor</td></tr>
	<tr><th scope=row>101</th><td>6.3</td><td>3.3</td><td>6</td><td>2.5</td><td>virginica</td></tr>
	<tr><th scope=row>102</th><td>5.8</td><td>2.7</td><td>5.1</td><td>1.9</td><td>virginica</td></tr>
	<tr><th scope=row>103</th><td>7.1</td><td>3</td><td>5.9</td><td>2.1</td><td>virginica</td></tr>
	<tr><th scope=row>104</th><td>6.3</td><td>2.9</td><td>5.6</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>105</th><td>6.5</td><td>3</td><td>5.8</td><td>2.2</td><td>virginica</td></tr>
	<tr><th scope=row>106</th><td>7.6</td><td>3</td><td>6.6</td><td>2.1</td><td>virginica</td></tr>
	<tr><th scope=row>107</th><td>4.9</td><td>2.5</td><td>4.5</td><td>1.7</td><td>virginica</td></tr>
	<tr><th scope=row>108</th><td>7.3</td><td>2.9</td><td>6.3</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>109</th><td>6.7</td><td>2.5</td><td>5.8</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>110</th><td>7.2</td><td>3.6</td><td>6.1</td><td>2.5</td><td>virginica</td></tr>
	<tr><th scope=row>111</th><td>6.5</td><td>3.2</td><td>5.1</td><td>2</td><td>virginica</td></tr>
	<tr><th scope=row>112</th><td>6.4</td><td>2.7</td><td>5.3</td><td>1.9</td><td>virginica</td></tr>
	<tr><th scope=row>113</th><td>6.8</td><td>3</td><td>5.5</td><td>2.1</td><td>virginica</td></tr>
	<tr><th scope=row>114</th><td>5.7</td><td>2.5</td><td>5</td><td>2</td><td>virginica</td></tr>
	<tr><th scope=row>115</th><td>5.8</td><td>2.8</td><td>5.1</td><td>2.4</td><td>virginica</td></tr>
	<tr><th scope=row>116</th><td>6.4</td><td>3.2</td><td>5.3</td><td>2.3</td><td>virginica</td></tr>
	<tr><th scope=row>117</th><td>6.5</td><td>3</td><td>5.5</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>118</th><td>7.7</td><td>3.8</td><td>6.7</td><td>2.2</td><td>virginica</td></tr>
	<tr><th scope=row>119</th><td>7.7</td><td>2.6</td><td>6.9</td><td>2.3</td><td>virginica</td></tr>
	<tr><th scope=row>120</th><td>6</td><td>2.2</td><td>5</td><td>1.5</td><td>virginica</td></tr>
	<tr><th scope=row>121</th><td>6.9</td><td>3.2</td><td>5.7</td><td>2.3</td><td>virginica</td></tr>
	<tr><th scope=row>122</th><td>5.6</td><td>2.8</td><td>4.9</td><td>2</td><td>virginica</td></tr>
	<tr><th scope=row>123</th><td>7.7</td><td>2.8</td><td>6.7</td><td>2</td><td>virginica</td></tr>
	<tr><th scope=row>124</th><td>6.3</td><td>2.7</td><td>4.9</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>125</th><td>6.7</td><td>3.3</td><td>5.7</td><td>2.1</td><td>virginica</td></tr>
	<tr><th scope=row>126</th><td>7.2</td><td>3.2</td><td>6</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>127</th><td>6.2</td><td>2.8</td><td>4.8</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>128</th><td>6.1</td><td>3</td><td>4.9</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>129</th><td>6.4</td><td>2.8</td><td>5.6</td><td>2.1</td><td>virginica</td></tr>
	<tr><th scope=row>130</th><td>7.2</td><td>3</td><td>5.8</td><td>1.6</td><td>virginica</td></tr>
	<tr><th scope=row>131</th><td>7.4</td><td>2.8</td><td>6.1</td><td>1.9</td><td>virginica</td></tr>
	<tr><th scope=row>132</th><td>7.9</td><td>3.8</td><td>6.4</td><td>2</td><td>virginica</td></tr>
	<tr><th scope=row>133</th><td>6.4</td><td>2.8</td><td>5.6</td><td>2.2</td><td>virginica</td></tr>
	<tr><th scope=row>134</th><td>6.3</td><td>2.8</td><td>5.1</td><td>1.5</td><td>virginica</td></tr>
	<tr><th scope=row>135</th><td>6.1</td><td>2.6</td><td>5.6</td><td>1.4</td><td>virginica</td></tr>
	<tr><th scope=row>136</th><td>7.7</td><td>3</td><td>6.1</td><td>2.3</td><td>virginica</td></tr>
	<tr><th scope=row>137</th><td>6.3</td><td>3.4</td><td>5.6</td><td>2.4</td><td>virginica</td></tr>
	<tr><th scope=row>138</th><td>6.4</td><td>3.1</td><td>5.5</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>139</th><td>6</td><td>3</td><td>4.8</td><td>1.8</td><td>virginica</td></tr>
	<tr><th scope=row>140</th><td>6.9</td><td>3.1</td><td>5.4</td><td>2.1</td><td>virginica</td></tr>
	<tr><th scope=row>141</th><td>6.7</td><td>3.1</td><td>5.6</td><td>2.4</td><td>virginica</td></tr>
	<tr><th scope=row>142</th><td>6.9</td><td>3.1</td><td>5.1</td><td>2.3</td><td>virginica</td></tr>
	<tr><th scope=row>143</th><td>5.8</td><td>2.7</td><td>5.1</td><td>1.9</td><td>virginica</td></tr>
	<tr><th scope=row>144</th><td>6.8</td><td>3.2</td><td>5.9</td><td>2.3</td><td>virginica</td></tr>
	<tr><th scope=row>145</th><td>6.7</td><td>3.3</td><td>5.7</td><td>2.5</td><td>virginica</td></tr>
	<tr><th scope=row>146</th><td>6.7</td><td>3</td><td>5.2</td><td>2.3</td><td>virginica</td></tr>
	<tr><th scope=row>147</th><td>6.3</td><td>2.5</td><td>5</td><td>1.9</td><td>virginica</td></tr>
	<tr><th scope=row>148</th><td>6.5</td><td>3</td><td>5.2</td><td>2</td><td>virginica</td></tr>
	<tr><th scope=row>149</th><td>6.2</td><td>3.4</td><td>5.4</td><td>2.3</td><td>virginica</td></tr>
	<tr><th scope=row>150</th><td>5.9</td><td>3</td><td>5.1</td><td>1.8</td><td>virginica</td></tr>
</tbody>
</table>





```R
summary(iris)
```




      Sepal.Length    Sepal.Width     Petal.Length    Petal.Width   
     Min.   :4.300   Min.   :2.000   Min.   :1.000   Min.   :0.100  
     1st Qu.:5.100   1st Qu.:2.800   1st Qu.:1.600   1st Qu.:0.300  
     Median :5.800   Median :3.000   Median :4.350   Median :1.300  
     Mean   :5.843   Mean   :3.057   Mean   :3.758   Mean   :1.199  
     3rd Qu.:6.400   3rd Qu.:3.300   3rd Qu.:5.100   3rd Qu.:1.800  
     Max.   :7.900   Max.   :4.400   Max.   :6.900   Max.   :2.500  
           Species  
     setosa    :50  
     versicolor:50  
     virginica :50  
                    
                    
                    




```R

```
