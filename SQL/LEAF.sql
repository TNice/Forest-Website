CREATE TABLE HUMAN (
  Agricultiral_Population <type>,
  Harvesting <type>,
  Mining <type>
);

CREATE TABLE REGION (
  Id <type> primary key,
  Year <type>
);

CREATE TABLE HYDROLOGY (
  Dist_To_Water_Body <type>,
  Dry_Farmland_Area_Proportion <type>,
  Paddy_Field_Area_Proportion <type>
);

/*Needs Attention*/
CREATE TABLE REPORTS_HUMAN (
  Field <type>,
  Field <type>,
  Field <type>
);

CREATE TABLE CLIMATE (
  Id <type> primary key,
  Min_Temp <type>,
  Max_Temp <type>,
  Avg_Temp <type>,
  Exavpotranspiration_Ratio <type>,
  Humidity <type>,
  Precipitation <type>,
  Wind <type>,
  Pressure <type>
);

/*Needs Attention*/
CREATE TABLE REPORTS_FIRE (
  Field <type>,
  Field <type>,
  Field <type>
);

/*Needs Attention*/
CREATE TABLE REPORTS_WIND (
  Field <type>,
  Field <type>,
  Field <type>
);

/*Needs Attention*/
CREATE TABLE REPORTS_BIOLOGICAL (
  Field <type>,
  Field <type>,
  Field <type>
);

CREATE TABLE USERS (
  Id <type> primary key,
  Name <type>,
  Field <type>
);

CREATE TABLE SPECIES (
  Name <type> primary key,
  Longevity <type>,
  Mature_Age <type>,
  Shade_Tolerance <type>,
  Fire_Tolerance <type>,
  Effective_Seeding_Distance <type>,
  Max_Seeding_Distance <type>,
  Vegetative_Propagation_Probability <type>,
  Min_Sprouting_Age <type>,
  Max_Sprouting_Age <type>,
  Reclassification_Coefficent <type>,
  Species_Group <type>,
  Biomass_Group <type>,
  Maximum_Diameter <type>,
  Maximum_Stand Density <type>,
  Number_of_Seeds <type>,
  Carbon_Coeffecient <type>,
  Seeding <type>,
  Growing_Space <type>,
  Min_Age_Cohort <type>,
  Max_Age_Cohort <type>,
  Basal_Area <type>
);

CREATE TABLE LOCATION (
  *X <type>,
  *Y <type>,
  Field <type>
  primary key(X, Y)
);

CREATE TABLE RESULTS (
  Analysis_Outcome <type>
);

CREATE TABLE FIRE_MAP (
  Fire_Boundary <type>,
  Fire_Size <type>,
  Time_Period <type>
);

CREATE TABLE TOPOGRAPHY (
  Terrain_Map <type>,
  Soil_Type <type>,
  Land_Type <type>
);

CREATE TABLE REPORTS (
  ReportId <type> primary key,
  Year <type>,
  Dataset_Description <type>,
  RegionId <type>
);

/*Needs Attention*/
CREATE TABLE REPORTS_SUCESSION (
  Field <type>,
  Field <type>,
  Field <type>
);

CREATE TABLE ANALYSIS_REQUESTS (
  UserId <type> primary key,
  Type <type>,
  Time <type>
);