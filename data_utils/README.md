# Database

The database is composed of 3 tables:
- Solar direct tree family
- Conjugal partners and recomposed family members in two tables

As well as a metadata table for extra information such as surname, profession, data of death, etc.

## Encodings

### Solar family tree

The fields of the Solar family tree table are:
- Names;  Father familyname; Mother familyname; Date of birth; Generation; Number; Unique ID; Relative UID;

Some fields follow more specific rules:
- Generation; The generation is the generation of the parent plus one; e.g. Miguel Angel Solar Silva is 0, Maria Olga is 1, Oscar Matias is 2, etc.
- Gen Number; The number ordered by birth date within a generation, Sebastian Gomez Solar (ID201) has 01 as he's the first family grandchildren, and Rafael Pizarro Solar (ID235) has 35 as he's the last of the 35 grandchildren.
- Unique ID: concat of fields GENERATION|GEN NUMBER; The unique ID for the family member.
- Relative UID; The ID of the solar relative that gave birth to the family member, example Matías González Montes (ID302), son of Óscar Matias González Solar (ID202), has 202 as Relative UID.

A full example with 'María Almendra García-Huidobro Venegas':
- Names: Maria Almendra
- Father familyname: García-Huidobro
- Mother familyname: Venegas
- Date of Birth: 12/06/96
- Generation: 3; with lineage of Anita Solar Silva (gen 1), Jorge Garcia-Huidobro Solar of (gen 2).
- Gen Number: 5; She has 4 people born before her in generation 3: Maria Jesus (01), Matias Gonzalez (02), Isidora Gonzalez (03), and Felipe Gonzales (04).
- Unique ID: 305; using her generation 3, with her number within her generation, Almendra has UID of 305.
- Relative ID: 206; She's the daughter of Jorge Garcia-Huidobro Solar, who's UID is 206.

### Conjugal family

Here we can include the parners of the family members, as well as their children in case of recomposed family.

On these table we have the same fields as for the Solar family tree, but their encoding changes:
- Names; Father familyname; Mother familyname; Date of birth; Generation; Number; Unique ID; Relative UID;

For the encoding, we use the following rules:
- Generation; 
  - Conjugal partner: The generation matches their Solar partner generation, for example the wifes and husband of a grandchildren, gen 2, would be gen 2 aswell. And for 
  - Conjugal family: The children are the generation of the parent plus one.
- Number
  - Conjugal partner: In case of multiple partners, the first one is 01, the second one 02, etc.
  - Conjugal family: For children from the same partner, ordered by birth date.
- Unique ID; 
  - Conjugal partner: Concat of RELATIVE ID|NUMBER. 
  - Conjugal family Concat of UID of Conjugal Parent|Number
- Relative ID;
  - Conjugal partner: The UID of the Solar relative
  - Conjugal family: The UID of the Solar relative


