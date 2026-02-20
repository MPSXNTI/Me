<!--
<details><summary></summary>

</details>

<details><summary></summary>

```lua
```
</details>

```ini
```

'97 ADI Bushmaster ----- PERFECT SHELTER 11202, 8276 -----
"C:\Program Files (x86)\Steam\steamapps\workshop\content\108600\2897390033\mods\97bushmaster\media\lua\server\97bushmaster_server.lua"

saved_outfits.txt
Daryl Dixon - Insurgent:gender=2;skincolor=1,0.91,0.72;name=Daryl|Dixon;hair=Grungey|0.5960784554481506,0.43921568989753723,0.2980392277240753;chesthair=2;beard=PointyChin;Hat=Insurgent.Hat_ArmyInsurgent;Pants=Insurgent.Trousers_Insurgent;Socks=Base.Socks_Ankle|1,1,1;Shoes=Base.Shoes_ArmyBoots;TorsoExtra=Insurgent.Vest_BulletArmyInsurgent;Jacket=Insurgent.Jacket_ArmyInsurgent;Mask=Insurgent.Hat_GasMaskInsurgent;BeltExtra=Base.HolsterSimple;Hands=Insurgent.Gloves_LongInsurgent;Necklace=Base.Necklace_DogTag;LeftWrist=Base.WristWatch_Left_DigitalBlack;
Magie Green - Insurgent:gender=1;skincolor=1,0.91,0.72;name=Magie|Green;hair=Grungey02|0.8313725590705872,0.6705882549285889,0.2705882489681244;Hat=Insurgent.Hat_ArmyInsurgent;Pants=Insurgent.Trousers_Insurgent;Socks=Base.Socks_Ankle|1,1,1;Shoes=Base.Shoes_ArmyBoots;TorsoExtra=Insurgent.Vest_BulletArmyInsurgent;Jacket=Insurgent.Jacket_ArmyInsurgent;Mask=Insurgent.Hat_GasMaskInsurgent;BeltExtra=Base.HolsterSimple;Hands=Insurgent.Gloves_LongInsurgent;Necklace=Base.Necklace_DogTag;LeftWrist=Base.WristWatch_Left_DigitalBlack;
Daryl Dixon:gender=2;skincolor=1,0.91,0.72;name=Daryl|Dixon;hair=Grungey|0.5960784554481506,0.43921568989753723,0.2980392277240753;chesthair=2;beard=PointyChin;Socks=Base.Socks_Ankle|1,1,1;
Magie Green:gender=1;skincolor=1,0.91,0.72;name=Magie|Green;hair=Grungey02|0.8313725590705872,0.6705882549285889,0.2705882489681244;Socks=Base.Socks_Ankle|1,1,1;
-->

---

<details><summary>Perfect Shelter</summary>

| Ubicacion archivos |
|--------------------|
| C:\Program Files (x86)\Steam\steamapps\workshop\content\108600\2860469874\mods\Perfect shelter\media\lua\server\items |

<details><summary>PerfectShelterTestsDistributions.lua</summary>

**Nota:** usar "{name="", min=1, max=100, weightChance=X},".

```lua


local PerfectShelterTable = {

--    Garage Food

    PS_Garage_Food = {

        shelves = {
            procedural = true,
            procList = {
                    }
            },
        crate = {
            procedural = true,
            procList = {
                    }
            },
		smallcrate = {
            procedural = true,
            procList = {
                    }
            },
        smallbox = {
            procedural = true,
            procList = {
                    }
            },	
        freezer = {
            procedural = true,
            procList = {
                    }
            },			
    },

--    Garage Weapons

    PS_Garage_Weapons = {

        metal_shelves = {
            procedural = true,
            procList = {
                    }
            },
        militarylocker = {
            procedural = true,
            procList = {
                    }
            },
    },

--    Main Storage
    PS_Hangar_Dressroom = {

        locker = {
            procedural = true,
            procList = {
                    }
            },
        clothingrack = {
            procedural = true,
            procList = {
                    }
            },	
    },
    PS_Hangar_Warehouse = {

        crate = {
            procedural = true,
            procList = {
                    }
            },
        metal_shelves = {
            procedural = true,
            procList = {
                    }
            },	
    },
    PS_Hangar_Workshop = {

        metal_shelves = {
            procedural = true,
            procList = {
                    }
            },
        militarylocker = {
            procedural = true,
            procList = {
                    }
            },
        toolcabinet = {
            procedural = true,
            procList = {
                    }
            },
        locker = {
            procedural = true,
            procList = {
                    }
            },
    },		
	
--    House	

    PS_House_Hall = {

        dishescabinet = {
            procedural = true,
            procList = {
                    }
            },
        wardrobe = {
            procedural = true,
            procList = {
                    }
            },
		sidetable = {
            procedural = true,
            procList = {
                    }
            },
        shelves = {
            procedural = true,
            procList = {
                    }
            },
    },			
    PS_House_Laundry = {

        clothingrack = {
            procedural = true,
            procList = {
                    }
            },
        clothingdryerbasic = {
            procedural = true,
            procList = {
                    }
            },
    },
    PS_House_Bathroom = {

        counter = {
            procedural = true,
            procList = {
                    }
            },
        medicine = {
            procedural = true,
            procList = {
                    }
            },
    },
    PS_House_Kitchen = {

        overhead = {
            procedural = true,
            procList = {
                    }
            },
        fridge = {
            procedural = true,
            procList = {
                    }
            },	
        counter = {
            procedural = true,
            procList = {
                    }
            },				
        freezer = {
            procedural = true,
            procList = {
                    }
            },			
    },	
    PS_House_Library = {

        locker = {
            procedural = true,
            procList = {
                    }
            },
		sidetable = {
            procedural = true,
            procList = {
                    }
            },
        shelves = {
            procedural = true,
            procList = {
                    }
            },				
    },	
    PS_House_Bedroom = {

        wardrobe = {
            procedural = true,
            procList = {
                    }
            },
		sidetable = {
            procedural = true,
            procList = {
                    }
            },
    },
	
--    Post
	
    PS_Post_WatchRoom = {

        locker = {
            procedural = true,
            procList = {
                    }
            },
        desk = {
            procedural = true,
            procList = {
                    }
            },
        filingcabinet = {
            procedural = true,
            procList = {
                    }
            },
    },	
    PS_Post_Bedroom = {

        locker = {
            procedural = true,
            procList = {
                    }
            },
        fridge = {
            procedural = true,
            procList = {
                    }
            },
        freezer = {
            procedural = true,
            procList = {
                    }
            },					
    },
	
--    FishShop

    PS_Shop_Hall = {

        metal_shelves = {
            procedural = true,
            procList = {
                    }
            },
        crate = {
            procedural = true,
            procList = {
                    }
            },
		smallcrate = {
            procedural = true,
            procList = {
                    }
            },
        smallbox = {
            procedural = true,
            procList = {
                    }
            },	
        counter = {
            procedural = true,
            procList = {
                    }
            },				
        freezer = {
            procedural = true,
            procList = {
                    }
            },			
    },	
    PS_Shop_Storage = {

        metal_shelves = {
            procedural = true,
            procList = {
                    }
            },
        crate = {
            procedural = true,
            procList = {
                    }
            },
		smallcrate = {
            procedural = true,
            procList = {
                    }
            },	
    },

}

table.insert(Distributions, 2, PerfectShelterTable);
```
</details>

<details><summary>PerfectShelterTestsProceduralDistributions.lua</summary>

```lua
local function preDistributionMerge()

-- Garage Food	
	
	    ProceduralDistributions.list.PS_Garage_Food_ = {
        rolls = 1,
        items = {
        },
    }

-- Garage Weapons

		ProceduralDistributions.list.PS_Garage_Weapons_ = {
        rolls = 1,
        items = {
        },
    }

-- Main Storage
	
	    ProceduralDistributions.list.PS_Hangar_Workshop_ = {
        rolls = 1,
        items = {
        },
    }
	    ProceduralDistributions.list.PS_Hangar_Warehouse_ = {
        rolls = 1,
        items = {
        },
    }
	    ProceduralDistributions.list.PS_Hangar_Dressroom_ = {
        rolls = 1,
        items = {
        },
    }

-- House

		ProceduralDistributions.list.PS_House_Hall_ = {
        rolls = 1,
        items = {
        },
    }
		ProceduralDistributions.list.PS_House_Bathroom_ = {
        rolls = 1,
        items = {
        },
    }
		ProceduralDistributions.list.PS_House_Kitchen_ = {
        rolls = 1,
        items = {
        },
    }
		ProceduralDistributions.list.PS_House_Library_ = {
        rolls = 1,
        items = {
        },
    }

-- FishShop

		ProceduralDistributions.list.PS_FishShop_Hall_ = {
        rolls = 1,
        items = {
        },
    }
		ProceduralDistributions.list.PS_FishShop_Storage_ = {
        rolls = 1,
        items = {
        },
    }


end
Events.OnPreDistributionMerge.Add(preDistributionMerge);
```

**Nota:** Lista de items para usar.

```lua
        ProceduralDistributions.list.PS_Hangar_Workshop_Medicalteam = {
        rolls = 1,
        items = {
            "Base.Antibiotics", 200,    --x20
            "Base.Pills", 200,          --x6
            "Base.AlcoholWipes", 200,   --x6
            "Base.Disinfectant", 200,   --x5
            "Base.AlcoholBandage", 200, --x5
            "Base.CottonBalls", 200,    --x4
            "Base.Bandaid", 200,        --x2
            "Base.Splint", 200,
            "Base.SutureNeedleHolder", 200,
            "Base.SutureNeedle", 200,
            "Base.Tweezers", 200,
        },
    }
```

```lua
        ProceduralDistributions.list.PS_Hangar_Workshop_Guns = {
        rolls = 3,
        items = {
            --Guns
            "Base.AssaultRifle", 200,
            --Weapon Part
            "Base.Laser", 200,
            "Base.RecoilPad", 200,
            "Base.RedDot", 200,
            --Ammo
            "Base.556Box", 200,
            "Base.556Box", 200,
            "Base.556Box", 200,
            "Base.556Box", 200,
            "Base.556Box", 200,
            "Base.556Box", 200,
            "Base.556Clip", 200,
            "Base.556Clip", 200,
            "Base.556Clip", 200,
            "Base.556Clip", 200,
            "Base.556Clip", 200,
        },
    }
```

```lua
        ProceduralDistributions.list.PS_Hangar_Workshop_Canned = {
        rolls = 3,
        items = {
            "CannedBolognese", 200,
            "CannedCarrots2", 200,
            "CannedChili", 200,
            "CannedCorn", 200,
            "CannedCornedBeef", 200,
            "CannedMushroomSoup", 200,
            "CannedPeaches", 200,
            "CannedPeas", 200,
            "CannedPineapple", 200,
            "CannedPotato2", 200,
            "CannedSardines", 200,
            "CannedTomato2", 200,
            "TinnedBeans", 200,
            "TinnedSoup", 200,
            "TunaTin", 200,
        },
    }
```

```lua
        ProceduralDistributions.list.PS_Hangar_Workshop_CarTools = {
        rolls = 1,
        items = {
            "PetrolCan", 200,
            "CarBatteryCharger", 200,
            "TirePump", 200,
            "LugWrench", 200,
            "Jack", 200,
            "MechanicMag1", 200,
            "MechanicMag2", 200,
            "MechanicMag3", 200,
        },
    }
```

```lua
	    ProceduralDistributions.list.PS_Hangar_Dressroom_equipment = {
        rolls = 1,
        items = {
            "Hat_Army", 200,
            "Hat_GasMask", 200,
            "Necklace_DogTag", 200,
            "Tshirt_CamoGreen", 200,
            "Shirt_CamoGreen", 200,
            "Jacket_ArmyCamoGreen", 200,
            "Vest_BulletArmy", 200,
            "Trousers_CamoGreen", 200,
            "Shoes_ArmyBoots", 200,
            "Gloves_LeatherGlovesBlack", 200,
            "HolsterSimple", 200,
            "Radio.WalkieTalkie5", 200,
            "Bag_ALICEpack_Army", 200,
        },
    }
```

```lua
        ProceduralDistributions.list.PS_Hangar_Workshop_Generator = {
        rolls = 1,
        items = {
            "Base.Generator", 200,
            "Base.PetrolCan", 200,
        },
    }
```

```lua
        ProceduralDistributions.list.PS_Hangar_Workshop_Tools = {
        rolls = 1,
        items = {
            --Metalworking
            "Base.WeldingMask", 200,
            "Base.BlowTorch", 200,
            "Base.WeldingRods", 200, --x5
            --Usefultools
            "Base.Wrench", 200,      --x5
            "Base.Hammer", 200,      --x4
            "Base.Screwdriver", 200, --x4
            "Base.Crowbar", 200,     --x3
            "Base.PipeWrench", 200,  --x2
            --Raretools
            "Base.Sledgehammer", 200,
            "Base.DuctTape", 200,
            "Base.WoodAxe", 200,
        },
    }
```

```lua
        ProceduralDistributions.list.PS_Hangar_Workshop_Metalworking = {
        rolls = 1,
        items = {
            "Base.MetalPipe", 200,
            "Base.MetalBar", 200,
            "Base.Wire", 200,
            "Base.BarbedWire", 200,
            "Base.ScrapMetal", 200,
            "Base.SheetMetal", 200,
            "Base.SmallSheetMetal", 200,
        },
    }
```

```lua
        ProceduralDistributions.list.PS_Hangar_Workshop_PropaneTank = {
        rolls = 1,
        items = {
            "Base.PropaneTank", 200,
        },
    }
```

```lua
		ProceduralDistributions.list.PS_House_Library_book01 = {
        rolls = 1,
        items = {
            "Base.BookCarpentry1", 200,
            "Base.BookCarpentry2", 200,
            "Base.BookCarpentry3", 200,
            "Base.BookCarpentry4", 200,
            "Base.BookCarpentry5", 200,
            "Base.BookCooking1", 200,
            "Base.BookCooking2", 200,
            "Base.BookCooking3", 200,
            "Base.BookCooking4", 200,
            "Base.BookCooking5", 200,
            "Base.BookElectrician1", 200,
            "Base.BookElectrician2", 200,
            "Base.BookElectrician3", 200,
            "Base.BookElectrician4", 200,
            "Base.BookElectrician5", 200,
            "Base.BookFarming1", 200,
            "Base.BookFarming2", 200,
            "Base.BookFarming3", 200,
            "Base.BookFarming4", 200,
            "Base.BookFarming5", 200,
            "Base.BookFirstAid1", 200,
            "Base.BookFirstAid2", 200,
            "Base.BookFirstAid3", 200,
            "Base.BookFirstAid4", 200,
            "Base.BookFirstAid5", 200,
        },
    }
```

```lua
		ProceduralDistributions.list.PS_House_Library_book02 = {
        rolls = 1,
        items = {
            "Base.BookForaging1", 200,
            "Base.BookForaging2", 200,
            "Base.BookForaging3", 200,
            "Base.BookForaging4", 200,
            "Base.BookForaging5", 200,
            "Base.BookMechanic1", 200,
            "Base.BookMechanic2", 200,
            "Base.BookMechanic3", 200,
            "Base.BookMechanic4", 200,
            "Base.BookMechanic5", 200,
            "Base.BookMetalWelding1", 200,
            "Base.BookMetalWelding2", 200,
            "Base.BookMetalWelding3", 200,
            "Base.BookMetalWelding4", 200,
            "Base.BookMetalWelding5", 200,
            "Base.BookTailoring1", 200,
            "Base.BookTailoring2", 200,
            "Base.BookTailoring3", 200,
            "Base.BookTailoring4", 200,
            "Base.BookTailoring5", 200,
            "Base.BookTrapping1", 200,
            "Base.BookTrapping2", 200,
            "Base.BookTrapping3", 200,
            "Base.BookTrapping4", 200,
            "Base.BookTrapping5", 200,
        },
    }
```

```lua
    	ProceduralDistributions.list.PS_House_Library_magazine = {
        rolls = 1,
        items = {
            "Base.BookFishing1", 200,
            "Base.BookFishing2", 200,
            "Base.BookFishing3", 200,
            "Base.BookFishing4", 200,
            "Base.BookFishing5", 200,
            "Base.FishingMag1", 200,
            "Base.FishingMag2", 200,
            "Base.ElectronicsMag1", 200,
            "Base.ElectronicsMag2", 200,
            "Base.ElectronicsMag3", 200,
            "Base.ElectronicsMag5", 200,
            "Base.EngineerMagazine1", 200,
            "Base.EngineerMagazine2", 200,
            "Base.CookingMag1", 200,
            "Base.CookingMag2", 200,
            "Radio.RadioMag1", 200,
            "Radio.RadioMag2", 200,
            "Radio.RadioMag3", 200,
            "Base.ElectronicsMag4", 200,
            "Base.MechanicMag1", 200,
            "Base.MechanicMag2", 200,
            "Base.MechanicMag3", 200,
            "Base.FarmingMag1", 200,
            "Base.HerbalistMag", 200,
            "Base.HuntingMag1", 200,
            "Base.HuntingMag2", 200,
            "Base.HuntingMag3", 200,
            "Base.MetalworkMag1", 200,
            "Base.MetalworkMag2", 200,
            "Base.MetalworkMag3", 200,
            "Base.MetalworkMag4", 200,
        },
    }
```

**Nota:** Lista de items de Mods.

```lua
		ProceduralDistributions.list.PS_Insurgent_Profession = {
        rolls = 1,
        items = {
            "Insurgent.Hat_ArmyInsurgent", 200,
            "Insurgent.Hat_GasMaskInsurgent", 200,
            "Necklace_DogTag", 200,
            "Tshirt_CamoUrban", 200,
            "Insurgent.Jacket_ArmyInsurgent", 200,
            "Insurgent.Vest_BulletArmyInsurgent", 200,
            "Insurgent.Trousers_Insurgent", 200,
            "Shoes_ArmyBoots", 200,
            "Insurgent.Gloves_LongInsurgent", 200,
            "HolsterSimple", 200,
            "Radio.WalkieTalkie5", 200,
            "Insurgent.Bag_ALICEpack_Insurgent", 200,
        },
    }
```

```lua
		ProceduralDistributions.list.PS_Brita_Weapon_Pack = {
        rolls = 1,
        items = {
            "Base.SCARL", 200,
            "Base.Sight_Aimpoint", 200,
            "Base.Sling_3", 200,
            "Base.Suppressor_Rifle", 200,
            "Base.Laser_Red", 200,
        },
    }
```

```lua
		ProceduralDistributions.list.PS_Snake_Mod_Pack = {
        rolls = 1,
        items = {
            --SniperRifleCammo
            "AmmoMaker.SniperRifleCammo", 200,
            "AmmoMaker.Ammo_762x39mm", 200,
            "AmmoMaker.762x39mmBox", 200,

            --Accesorios M16
            "WPA.M16BoltCarrier", 200,
            "WPA.M16LaserLight", 200,
            "WPA.M16Reflex", 200,
            "WPA.Silencerm16", 200,
            "WPA.M16RecoilPad", 200,

            --Accesorios M9
            "WPA.Slide1", 200,
            "WPA.LaserLight", 200,
            "WPA.Pistolx2Scope2", 200,
            "WPA.Supressor1", 200,
            "WPA.Grip1", 200,

            --AK-47
            "AmmoMaker.AK47", 200,
            "AmmoMaker.AKMMag", 200,
            "AmmoMaker.AKHG", 200,
            "AmmoMaker.AKTacticalLight", 200,
            "AmmoMaker.AK47MilitaryScope", 200,
            "AmmoMaker.SilencerAK", 200,
            "AmmoMaker.AKRecoilPad", 200

            --Caja de balas
            "AmmoMaker.556x45mmCan", 200,
            "AmmoMaker.9mmCan", 200,
            "AmmoMaker.762Can", 200,

            --Revista
            "AmmoMaker.WeaponsMagazine4", 200,
            "AmmoMaker.AmmoMagazine1", 200,
            "AmmoMaker.AmmoMagazine3", 200,
            "AmmoMaker.AmmoMagazine14", 200,
            "AmmoMaker.AmmoMagazine2", 200,
            "AmmoMaker.AmmoMagazine10", 200,
            "AmmoMaker.AmmoMagazine6", 200,
            "WPA.WeaponsMagazine", 200,
            "TableSaw.SawMag1", 200,

            --Mochila
            "AliceSPack.AlicePackSnake", 200,
        },
    }
```
</details>

</details>

---
---

<details><summary>Insurgent Profession</summary>

| Ubicacion archivos |
|--------------------|
| C:\Program Files (x86)\Steam\steamapps\workshop\content\108600\2907683021\mods\Insurgent Profession\media\lua\client |
| C:\Program Files (x86)\Steam\steamapps\workshop\content\108600\2907683021\mods\Insurgent Profession\media\lua\shared\Insurgent\Traits |

<details><summary>NavySEALsTrait.lua</summary>

```lua
require "Insurgent/InsurgentTraitDefinitions"

NavySEALsTrait = CreateInsurgentTrait()
NavySEALsTrait.name = "NavySEALs"
NavySEALsTrait.insurgentExclusive = true

function NavySEALsTrait.Create()
    local navyseals = TraitFactory.addTrait("NavySEALs", getText("UI_trait_NavySEALs"), 12, getText("UI_trait_NavySEALsDesc"), false, false);
    ----
    navyseals:addXPBoost(Perks.Fitness, 10);	
    navyseals:addXPBoost(Perks.Strength, 8);
    ----
    navyseals:addXPBoost(Perks.Sprinting, 7);
    navyseals:addXPBoost(Perks.Lightfoot, 6);
    navyseals:addXPBoost(Perks.Nimble, 7);
    navyseals:addXPBoost(Perks.Sneak, 9);
    ----
    navyseals:addXPBoost(Perks.Axe, 2);
    navyseals:addXPBoost(Perks.Blunt, 3);
    navyseals:addXPBoost(Perks.SmallBlunt, 3);
    navyseals:addXPBoost(Perks.LongBlade, 2);
    navyseals:addXPBoost(Perks.SmallBlade, 7);
    navyseals:addXPBoost(Perks.Spear, 1);
    navyseals:addXPBoost(Perks.Maintenance, 9);
    ----
    navyseals:addXPBoost(Perks.Woodwork, 3);
    navyseals:addXPBoost(Perks.Cooking, 4);
    navyseals:addXPBoost(Perks.Farming, 1);
    navyseals:addXPBoost(Perks.Doctor, 8);
    navyseals:addXPBoost(Perks.Electricity, 5);
    navyseals:addXPBoost(Perks.MetalWelding, 2);
    navyseals:addXPBoost(Perks.Mechanics, 6);
    navyseals:addXPBoost(Perks.Tailoring, 2);
    ----
    navyseals:addXPBoost(Perks.Aiming, 10);
    navyseals:addXPBoost(Perks.Reloading, 9);
    ----
    navyseals:addXPBoost(Perks.Fishing, 5);
    navyseals:addXPBoost(Perks.Trapping, 6);
    navyseals:addXPBoost(Perks.PlantScavenging, 5);
    ----
    return navyseals;
end

function NavySEALsTrait.OnNewGame(player)
    if not player:HasTrait("NavySEALs") then
        return
    end

    local weapon = InsurgentWeaponUtil.addWeapon(player, "Base.AssaultRifle", {"Base.Laser", "Base.RecoilPad", "Base.RedDot"})
    InsurgentWeaponUtil.addMags(player, "Base.556Clip", 2)
    InsurgentWeaponUtil.equipAndFullyLoadWeapon(player, weapon, "Base.556Clip")
end

function NavySEALsTrait.RegisterEvents()
    Events.OnNewGame.Add(NavySEALsTrait.OnNewGame)
end
```
</details>

<details><summary>GhostOpTrait.lua</summary>

```lua
require "Insurgent/InsurgentTraitDefinitions"

GhostOpTrait = CreateInsurgentTrait()
GhostOpTrait.name = "GhostOp"
GhostOpTrait.insurgentExclusive = true

function GhostOpTrait.Create()
    local ghostop = TraitFactory.addTrait("GhostOp", getText("UI_trait_GhostOp"), 12, getText("UI_trait_GhostOpDesc"), false, false);
    ----
    ghostop:addXPBoost(Perks.Fitness, 10);	
    ghostop:addXPBoost(Perks.Strength, 9);
    ----
    ghostop:addXPBoost(Perks.Sprinting, 7);
    ghostop:addXPBoost(Perks.Lightfoot, 9);
    ghostop:addXPBoost(Perks.Nimble, 9);
    ghostop:addXPBoost(Perks.Sneak, 10);
    ----
    ghostop:addXPBoost(Perks.Axe, 8);
    ghostop:addXPBoost(Perks.Blunt, 7);
    ghostop:addXPBoost(Perks.SmallBlunt, 7);
    ghostop:addXPBoost(Perks.LongBlade, 7);
    ghostop:addXPBoost(Perks.SmallBlade, 10);
    ghostop:addXPBoost(Perks.Spear, 8);
    ghostop:addXPBoost(Perks.Maintenance, 10);
    ----
    ghostop:addXPBoost(Perks.Woodwork, 8);
    ghostop:addXPBoost(Perks.Cooking, 7);
    ghostop:addXPBoost(Perks.Farming, 9);
    ghostop:addXPBoost(Perks.Doctor, 9);
    ghostop:addXPBoost(Perks.Electricity, 6);
    ghostop:addXPBoost(Perks.MetalWelding, 7);
    ghostop:addXPBoost(Perks.Mechanics, 8);
    ghostop:addXPBoost(Perks.Tailoring, 7);
    ----
    ghostop:addXPBoost(Perks.Aiming, 8);
    ghostop:addXPBoost(Perks.Reloading, 9);
    ----
    ghostop:addXPBoost(Perks.Fishing, 8);
    ghostop:addXPBoost(Perks.Trapping, 9);
    ghostop:addXPBoost(Perks.PlantScavenging, 9);
    ----
    --Base.FishingMag1
    ghostop:getFreeRecipes():add("Make Fishing Rod");
    ghostop:getFreeRecipes():add("Fix Fishing Rod");
    --Base.ElectronicsMag2
    ghostop:getFreeRecipes():add("Make Timer");
    ghostop:getFreeRecipes():add("Add Timer");
    --Base.ElectronicsMag5
    ghostop:getFreeRecipes():add("Make Remote Trigger");
    ghostop:getFreeRecipes():add("Add Crafted Trigger");
    --Base.EngineerMagazine2
    ghostop:getFreeRecipes():add("Make Smoke Bomb");
    --Base.CookingMag2
    ghostop:getFreeRecipes():add("Make Bread Dough");
    ghostop:getFreeRecipes():add("Make Biscuits");
    ghostop:getFreeRecipes():add("Make Pizza");
    --Base.FarmingMag1
    ghostop:getFreeRecipes():add("Make Mildew Cure");
    ghostop:getFreeRecipes():add("Make Flies Cure");
    --Base.HerbalistMag
    ghostop:getFreeRecipes():add("Herbalist");
    --Base.HuntingMag1
    ghostop:getFreeRecipes():add("Make Snare Trap");
    --Base.HuntingMag2
    ghostop:getFreeRecipes():add("Make Wooden Box Trap");
    ghostop:getFreeRecipes():add("Make Stick Trap");
    --Base.HuntingMag3
    ghostop:getFreeRecipes():add("Make Trap Box");
    ghostop:getFreeRecipes():add("Make Cage Trap");
    --Base.MetalworkMag1
    ghostop:getFreeRecipes():add("Make Metal Walls");
    ghostop:getFreeRecipes():add("Make Metal Roof");
    --Base.MetalworkMag2
    ghostop:getFreeRecipes():add("Make Metal Containers");
    --Base.MetalworkMag3
    ghostop:getFreeRecipes():add("Make Metal Fences");
    --Base.MetalworkMag4
    ghostop:getFreeRecipes():add("Make Metal Sheet");
    ghostop:getFreeRecipes():add("Make Small Metal Sheet");
    ----
    return ghostop;
end

function GhostOpTrait.OnNewGame(player)
    if not player:HasTrait("GhostOp") then
        return
    end

    local weapon = InsurgentWeaponUtil.addWeapon(player, "Base.HuntingRifle", {"Base.AmmoStraps", "Base.RecoilPad", "Base.x8Scope"})
    InsurgentWeaponUtil.addMags(player, "Base.308Clip", 4)
    InsurgentWeaponUtil.equipAndFullyLoadWeapon(player, weapon, "Base.308Clip")
end

function GhostOpTrait.RegisterEvents()
    Events.OnNewGame.Add(GhostOpTrait.OnNewGame)
end
```
</details>

<details><summary>WastelanderTrait.lua</summary>

```lua
require "Insurgent/InsurgentTraitDefinitions"

WastelanderTrait = CreateInsurgentTrait()
WastelanderTrait.name = "Wastelander"
WastelanderTrait.insurgentExclusive = true

function WastelanderTrait.Create()
    local wastelander = TraitFactory.addTrait("Wastelander", getText("UI_trait_Wastelander"), 12, getText("UI_trait_WastelanderDesc"), false, false);
    ----
    wastelander:addXPBoost(Perks.Fitness, 8);	
    wastelander:addXPBoost(Perks.Strength, 7);
    ----
    wastelander:addXPBoost(Perks.Sprinting, 6);
    wastelander:addXPBoost(Perks.Lightfoot, 8);
    wastelander:addXPBoost(Perks.Nimble, 8);
    wastelander:addXPBoost(Perks.Sneak, 9);
    ----
    wastelander:addXPBoost(Perks.Axe, 9);
    wastelander:addXPBoost(Perks.Blunt, 7);
    wastelander:addXPBoost(Perks.SmallBlunt, 7);
    wastelander:addXPBoost(Perks.LongBlade, 8);
    wastelander:addXPBoost(Perks.SmallBlade, 10);
    wastelander:addXPBoost(Perks.Spear, 9);
    wastelander:addXPBoost(Perks.Maintenance, 8);
    ----
    wastelander:addXPBoost(Perks.Woodwork, 9);
    wastelander:addXPBoost(Perks.Cooking, 8);
    wastelander:addXPBoost(Perks.Farming, 10);
    wastelander:addXPBoost(Perks.Doctor, 6);
    wastelander:addXPBoost(Perks.Electricity, 4);
    wastelander:addXPBoost(Perks.MetalWelding, 6);
    wastelander:addXPBoost(Perks.Mechanics, 7);
    wastelander:addXPBoost(Perks.Tailoring, 8);
    ----
    wastelander:addXPBoost(Perks.Aiming, 5);
    wastelander:addXPBoost(Perks.Reloading, 8);
    ----
    wastelander:addXPBoost(Perks.Fishing, 9);
    wastelander:addXPBoost(Perks.Trapping, 10);
    wastelander:addXPBoost(Perks.PlantScavenging, 10);
    ----
    --Base.FishingMag1
    wastelander:getFreeRecipes():add("Make Fishing Rod");
    wastelander:getFreeRecipes():add("Fix Fishing Rod");
    --Base.CookingMag2
    wastelander:getFreeRecipes():add("Make Bread Dough");
    wastelander:getFreeRecipes():add("Make Biscuits");
    wastelander:getFreeRecipes():add("Make Pizza");
    --Base.FarmingMag1
    wastelander:getFreeRecipes():add("Make Mildew Cure");
    wastelander:getFreeRecipes():add("Make Flies Cure");
    --Base.HerbalistMag
    wastelander:getFreeRecipes():add("Herbalist");
    --Base.HuntingMag1
    wastelander:getFreeRecipes():add("Make Snare Trap");
    --Base.HuntingMag2
    wastelander:getFreeRecipes():add("Make Wooden Box Trap");
    wastelander:getFreeRecipes():add("Make Stick Trap");
    --Base.HuntingMag3
    wastelander:getFreeRecipes():add("Make Trap Box");
    wastelander:getFreeRecipes():add("Make Cage Trap");
    --Base.MetalworkMag1
    wastelander:getFreeRecipes():add("Make Metal Walls");
    wastelander:getFreeRecipes():add("Make Metal Roof");
    --Base.MetalworkMag2
    wastelander:getFreeRecipes():add("Make Metal Containers");
    --Base.MetalworkMag3
    wastelander:getFreeRecipes():add("Make Metal Fences");
    --Base.MetalworkMag4
    wastelander:getFreeRecipes():add("Make Metal Sheet");
    wastelander:getFreeRecipes():add("Make Small Metal Sheet");
    ----
    return wastelander;
end

function WastelanderTrait.OnNewGame(player)
    if not player:HasTrait("Wastelander") then
        return
    end

    player:getInventory():AddItem("Base.Machete");

    local weapon = InsurgentWeaponUtil.addWeapon(player, "Base.DoubleBarrelShotgun", {"Base.AmmoStraps", "Base.RecoilPad"})
    InsurgentWeaponUtil.addMags(player, "Base.ShotgunShellsBox", 2)
    InsurgentWeaponUtil.equipAndFullyLoadWeapon(player, weapon, "Base.ShotgunShells")
end

function WastelanderTrait.RegisterEvents()
    Events.OnNewGame.Add(WastelanderTrait.OnNewGame)
end
```
</details>

<details><summary>CIATrait.lua</summary>

```lua
require "Insurgent/InsurgentTraitDefinitions"

CIATrait = CreateInsurgentTrait()
CIATrait.name = "CIA"
CIATrait.insurgentExclusive = true

function CIATrait.Create()
    local cia = TraitFactory.addTrait("CIA", getText("UI_trait_CIA"), 12, getText("UI_trait_CIADesc"), false, false);
    ----
    cia:addXPBoost(Perks.Fitness, 7);	
    cia:addXPBoost(Perks.Strength, 6);
    ----
    cia:addXPBoost(Perks.Sprinting, 6);
    cia:addXPBoost(Perks.Lightfoot, 9);
    cia:addXPBoost(Perks.Nimble, 8);
    cia:addXPBoost(Perks.Sneak, 10);
    ----
    cia:addXPBoost(Perks.Axe, 2);
    cia:addXPBoost(Perks.Blunt, 5);
    cia:addXPBoost(Perks.SmallBlunt, 6);
    cia:addXPBoost(Perks.LongBlade, 3);
    cia:addXPBoost(Perks.SmallBlade, 8);
    cia:addXPBoost(Perks.Spear, 1);
    cia:addXPBoost(Perks.Maintenance, 5);
    ----
    cia:addXPBoost(Perks.Woodwork, 2);
    cia:addXPBoost(Perks.Cooking, 5);
    cia:addXPBoost(Perks.Farming, 1);
    cia:addXPBoost(Perks.Doctor, 6);
    cia:addXPBoost(Perks.Electricity, 8);
    cia:addXPBoost(Perks.MetalWelding, 3);
    cia:addXPBoost(Perks.Mechanics, 6);
    cia:addXPBoost(Perks.Tailoring, 4);
    ----
    cia:addXPBoost(Perks.Aiming, 7);
    cia:addXPBoost(Perks.Reloading, 6);
    ----
    cia:addXPBoost(Perks.Fishing, 3);
    cia:addXPBoost(Perks.Trapping, 4);
    cia:addXPBoost(Perks.PlantScavenging, 5);
    ----
    return cia;
end
```
</details>

<details><summary>OfficerTrait.lua</summary>

```lua
require "Insurgent/InsurgentTraitDefinitions"

OfficerTrait = CreateInsurgentTrait()
OfficerTrait.name = "Officer"
OfficerTrait.insurgentExclusive = true

function OfficerTrait.Create()
    local officer = TraitFactory.addTrait("Officer", getText("UI_trait_Officer"), 12, getText("UI_trait_OfficerDesc"), false, false);
    ----
    officer:addXPBoost(Perks.Fitness, 7);	
    officer:addXPBoost(Perks.Strength, 6);
    ----
    officer:addXPBoost(Perks.Sprinting, 7);
    officer:addXPBoost(Perks.Lightfoot, 4);
    officer:addXPBoost(Perks.Nimble, 6);
    officer:addXPBoost(Perks.Sneak, 3);
    ----
    officer:addXPBoost(Perks.Axe, 2);
    officer:addXPBoost(Perks.Blunt, 6);
    officer:addXPBoost(Perks.SmallBlunt, 7);
    officer:addXPBoost(Perks.LongBlade, 1);
    officer:addXPBoost(Perks.SmallBlade, 5);
    officer:addXPBoost(Perks.Spear, 1);
    officer:addXPBoost(Perks.Maintenance, 5);
    ----
    officer:addXPBoost(Perks.Woodwork, 2);
    officer:addXPBoost(Perks.Cooking, 6);
    officer:addXPBoost(Perks.Farming, 1);
    officer:addXPBoost(Perks.Doctor, 5);
    officer:addXPBoost(Perks.Electricity, 4);
    officer:addXPBoost(Perks.MetalWelding, 2);
    officer:addXPBoost(Perks.Mechanics, 4);
    officer:addXPBoost(Perks.Tailoring, 2);
    ----
    officer:addXPBoost(Perks.Aiming, 6);
    officer:addXPBoost(Perks.Reloading, 4);
    ----
    officer:addXPBoost(Perks.Fishing, 3);
    officer:addXPBoost(Perks.Trapping, 2);
    officer:addXPBoost(Perks.PlantScavenging, 2);
    ----
    return officer;
end

function OfficerTrait.OnNewGame(player)
    if not player:HasTrait("Officer") then
        return
    end

    player:getInventory():AddItem("Base.Nightstick");

    local weapon = InsurgentWeaponUtil.addWeapon(player, "Base.Shotgun", {"Base.AmmoStraps", "Base.ChokeTubeFull", "Base.RecoilPad", "Base.x2Scope"})
    InsurgentWeaponUtil.addMags(player, "Base.ShotgunShellsBox", 2)
    InsurgentWeaponUtil.equipAndFullyLoadWeapon(player, weapon, "Base.ShotgunShells")
end

function OfficerTrait.RegisterEvents()
    Events.OnNewGame.Add(OfficerTrait.OnNewGame)
end
```
</details>

<details><summary>CivilianTrait.lua</summary>

```lua
require "Insurgent/InsurgentTraitDefinitions"

CivilianTrait = CreateInsurgentTrait()
CivilianTrait.name = "Civilian"
CivilianTrait.insurgentExclusive = true

function CivilianTrait.Create()
    local civilian = TraitFactory.addTrait("Civilian", getText("UI_trait_Civilian"), 12, getText("UI_trait_CivilianDesc"), false, false);
    ----
    civilian:addXPBoost(Perks.Fitness, 5);	
    civilian:addXPBoost(Perks.Strength, 5);
    ----
    civilian:addXPBoost(Perks.Sprinting, 5);
    civilian:addXPBoost(Perks.Lightfoot, 3);
    civilian:addXPBoost(Perks.Nimble, 4);
    civilian:addXPBoost(Perks.Sneak, 2);
    ----
    civilian:addXPBoost(Perks.Axe, 2);
    civilian:addXPBoost(Perks.Blunt, 3);
    civilian:addXPBoost(Perks.SmallBlunt, 3);
    civilian:addXPBoost(Perks.LongBlade, 1);
    civilian:addXPBoost(Perks.SmallBlade, 4);
    civilian:addXPBoost(Perks.Spear, 1);
    civilian:addXPBoost(Perks.Maintenance, 3);
    ----
    civilian:addXPBoost(Perks.Woodwork, 2);
    civilian:addXPBoost(Perks.Cooking, 7);
    civilian:addXPBoost(Perks.Farming, 3);
    civilian:addXPBoost(Perks.Doctor, 3);
    civilian:addXPBoost(Perks.Electricity, 4);
    civilian:addXPBoost(Perks.MetalWelding, 1);
    civilian:addXPBoost(Perks.Mechanics, 3);
    civilian:addXPBoost(Perks.Tailoring, 5);
    ----
    civilian:addXPBoost(Perks.Aiming, 2);
    civilian:addXPBoost(Perks.Reloading, 1);
    ----
    civilian:addXPBoost(Perks.Fishing, 3);
    civilian:addXPBoost(Perks.Trapping, 2);
    civilian:addXPBoost(Perks.PlantScavenging, 3);
    ----
    --Base.CookingMag1
    civilian:getFreeRecipes():add("Make Cake Batter");
    civilian:getFreeRecipes():add("Make Pie Dough");
    civilian:getFreeRecipes():add("Make Chocolate Chip Cookie Dough");
    civilian:getFreeRecipes():add("Make Chocolate Cookie Dough");
    civilian:getFreeRecipes():add("Make Oatmeal Cookie Dough");
    civilian:getFreeRecipes():add("Make Sugar Cookie Dough");
    civilian:getFreeRecipes():add("Make Shortbread Cookie Dough");
    --Base.CookingMag2
    civilian:getFreeRecipes():add("Make Bread Dough");
    civilian:getFreeRecipes():add("Make Biscuits");
    civilian:getFreeRecipes():add("Make Pizza");
    return civilian;
end

function CivilianTrait.OnNewGame(player)
    if not player:HasTrait("Civilian") then
        return
    end

    player:getInventory():AddItem("Base.BaseballBatNails");
end

function CivilianTrait.RegisterEvents()
    Events.OnNewGame.Add(CivilianTrait.OnNewGame)
end
```
</details>

<details><summary>Additional</summary>

**Nota:** function *xTrait.Create()* limpia (cambiar todo donde salga *string* or *int*).

```lua
require "Insurgent/InsurgentTraitDefinitions"

StringTrait = CreateInsurgentTrait()
StringTrait.name = "String"
StringTrait.insurgentExclusive = true

function StringTrait.Create()
    local string = TraitFactory.addTrait("String", getText("UI_trait_String"), int, getText("UI_trait_StringDesc"), false, false);
    ----
    string:addXPBoost(Perks.Fitness, int);	
    string:addXPBoost(Perks.Strength, int);
    ----
    string:addXPBoost(Perks.Sprinting, int);
    string:addXPBoost(Perks.Lightfoot, int);
    string:addXPBoost(Perks.Nimble, int);
    string:addXPBoost(Perks.Sneak, int);
    ----
    string:addXPBoost(Perks.Axe, int);
    string:addXPBoost(Perks.Blunt, int);
    string:addXPBoost(Perks.SmallBlunt, int);
    string:addXPBoost(Perks.LongBlade, int);
    string:addXPBoost(Perks.SmallBlade, int);
    string:addXPBoost(Perks.Spear, int);
    string:addXPBoost(Perks.Maintenance, int);
    ----
    string:addXPBoost(Perks.Woodwork, int);
    string:addXPBoost(Perks.Cooking, int);
    string:addXPBoost(Perks.Farming, int);
    string:addXPBoost(Perks.Doctor, int);
    string:addXPBoost(Perks.Electricity, int);
    string:addXPBoost(Perks.MetalWelding, int);
    string:addXPBoost(Perks.Mechanics, int);
    string:addXPBoost(Perks.Tailoring, int);
    ----
    string:addXPBoost(Perks.Aiming, int);
    string:addXPBoost(Perks.Reloading, int);
    ----
    string:addXPBoost(Perks.Fishing, int);
    string:addXPBoost(Perks.Trapping, int);
    string:addXPBoost(Perks.PlantScavenging, int);
    ----
    return string;
end
```

**Nota:** Opcional si se quieren agregar armas u objetos al Trait.

```lua
function StringTrait.OnNewGame(player)
    if not player:HasTrait("String") then
        return
    end

    player:getInventory():AddItem("Base.Sledgehammer");

    local weapon = InsurgentWeaponUtil.addWeapon(player, "Base.Shotgun", {"Base.AmmoStraps", "Base.ChokeTubeFull", "Base.RecoilPad", "Base.x2Scope"})
    InsurgentWeaponUtil.addMags(player, "Base.ShotgunShellsBox", 2)
    InsurgentWeaponUtil.equipAndFullyLoadWeapon(player, weapon, "Base.ShotgunShells")
end

function StringTrait.RegisterEvents()
    Events.OnNewGame.Add(StringTrait.OnNewGame)
end
```

**Nota:** SkillBook, poner dentro de function *xTrait.Create()*.

```lua
    --Base.FishingMag1
    x:getFreeRecipes():add("Make Fishing Rod");
    x:getFreeRecipes():add("Fix Fishing Rod");
    --Base.FishingMag2
    x:getFreeRecipes():add("Make Fishing Net");
    x:getFreeRecipes():add("Get Wire Back");
    --Base.ElectronicsMag1
    x:getFreeRecipes():add("Make Remote Controller V1");
    x:getFreeRecipes():add("Make Remote Controller V2");
    x:getFreeRecipes():add("Make Remote Controller V3");
    --Base.ElectronicsMag2
    x:getFreeRecipes():add("Make Timer");
    x:getFreeRecipes():add("Add Timer");
    --Base.ElectronicsMag3
    x:getFreeRecipes():add("Add Motion Sensor V1");
    x:getFreeRecipes():add("Add Motion Sensor V2");
    x:getFreeRecipes():add("Add Motion Sensor V3");
    --Base.ElectronicsMag5
    x:getFreeRecipes():add("Make Remote Trigger");
    x:getFreeRecipes():add("Add Crafted Trigger");
    --Base.EngineerMagazine1
    x:getFreeRecipes():add("Make Noise Maker");
    --Base.EngineerMagazine2
    x:getFreeRecipes():add("Make Smoke Bomb");
    --Base.CookingMag1
    x:getFreeRecipes():add("Make Cake Batter");
    x:getFreeRecipes():add("Make Pie Dough");
    x:getFreeRecipes():add("Make Chocolate Chip Cookie Dough");
    x:getFreeRecipes():add("Make Chocolate Cookie Dough");
    x:getFreeRecipes():add("Make Oatmeal Cookie Dough");
    x:getFreeRecipes():add("Make Sugar Cookie Dough");
    x:getFreeRecipes():add("Make Shortbread Cookie Dough");
    --Base.CookingMag2
    x:getFreeRecipes():add("Make Bread Dough");
    x:getFreeRecipes():add("Make Biscuits");
    x:getFreeRecipes():add("Make Pizza");
    --Radio.RadioMag1
    x:getFreeRecipes():add("Craft Makeshift Radio");
    --Radio.RadioMag2
    x:getFreeRecipes():add("Craft Makeshift Walkie Talkie");
    --Radio.RadioMag3
    x:getFreeRecipes():add("Craft Makeshift HAM Radio");
    --Base.ElectronicsMag4
    x:getFreeRecipes():add("Generator");
    --Base.MechanicMag1
    x:getFreeRecipes():add("Basic Mechanics");
    --Base.MechanicMag2
    x:getFreeRecipes():add("Intermediate Mechanics");
    --Base.MechanicMag3
    x:getFreeRecipes():add("Advanced Mechanics");
    --Base.FarmingMag1
    x:getFreeRecipes():add("Make Mildew Cure");
    x:getFreeRecipes():add("Make Flies Cure");
    --Base.HerbalistMag
    x:getFreeRecipes():add("Herbalist");
    --Base.HuntingMag1
    x:getFreeRecipes():add("Make Snare Trap");
    --Base.HuntingMag2
    x:getFreeRecipes():add("Make Wooden Box Trap");
    x:getFreeRecipes():add("Make Stick Trap");
    --Base.HuntingMag3
    x:getFreeRecipes():add("Make Trap Box");
    x:getFreeRecipes():add("Make Cage Trap");
    --Base.MetalworkMag1
    x:getFreeRecipes():add("Make Metal Walls");
    x:getFreeRecipes():add("Make Metal Roof");
    --Base.MetalworkMag2
    x:getFreeRecipes():add("Make Metal Containers");
    --Base.MetalworkMag3
    x:getFreeRecipes():add("Make Metal Fences");
    --Base.MetalworkMag4
    x:getFreeRecipes():add("Make Metal Sheet");
    x:getFreeRecipes():add("Make Small Metal Sheet");
    ----
```
</details>

</details>

---
---

<details><summary>OBJETOS que SIEMPRE DEBEMOS de LOOTEAR │ GUIA para PRINCIPIANTES │ PROJECT ZOMBOID.txt</summary>

OBJETOS que SIEMPRE DEBEMOS de LOOTEAR │ GUIA para PRINCIPIANTES │ PROJECT ZOMBOID
---
https://www.youtube.com/watch?v=lfBsjWLfF6M
---
Qué onda gente YouTube aquí pirata pingüino y les Traigo una nueva guía de projection void hoy vamos a hablar de uno de los problemas que creo que todos hemos tenido cuando iniciamos a jugar un juego de supervivencia y es saber qué objetos agarrar y cuáles no realmente todos o casi todos los objetos en proyección void tienen una utilidad sin embargo no podremos luchar todos los objetos al mismo tiempo en especial en juego temprano donde no Tendremos una base establecida y deberemos de llevar muchos de estos objetos en nuestro inventario y si nos terminamos llevando objetos poco útiles podremos perder la oportunidad de llevar algún objeto que sea esencial por lo que hay que saber priorizar algunos objetos sobre otros Así que hablaremos de objetos que siempre debemos de luchar en cualquier partida objetos de primeros auxilios los objetos de primeros auxilios son bastante importantes en este juego y aun cuando siempre intentaremos hacernos el menor daño posible debemos estar preparados para cualquier tipo de emergencia por eso siempre debemos de luchar vendas y tiritas que nos servirán para detener las hemorragias y ayudar a curar cualquier tipo de herida sin embargo si no llegamos a encontrarlos siempre podremos ocupar retales de tela que harán la misma función por otro lado si la herida que tenemos es profunda necesitaremos ocupar aguja de sutura para poder cerrar la herida ya que si solo ocupamos las vendas la herida tardará mucho más tiempo en curarse también hay que tomar en cuenta que cualquier herida podrá infectarse lo que retrasará el tiempo de curación Y aumentará el dolor que tenemos por lo que será útil tener algún objeto desinfectante a la mano como las toallitas de alcohol los antibióticos y el bote de desinfectante los objetos de primeros auxilios también servirán para eliminar algunos estados los analgésicos servirán para eliminar el estado de dolor los antidepresivos para eliminar el estado de infelicidad las vitaminas para eliminar un poco del estado de cansado y los tranquilizantes eliminarán el estado de pánico todos estos objetos de primeros auxilios los podremos encontrar en los botiquines los baños de Las Casas Las ambulancias y en los edificios médicos como las farmacias hospitales y consultorios médicos estos edificios siempre aparecerán de color rosa en el mapa armas Cuerpo A Cuerpo y materiales de reparación otros objetos fundamentales en este juego Serán las armas Cuerpo A Cuerpo todas las armas serán útiles para defendernos dependiendo de lo avanzada que esté la partida por lo que nunca hay que despreciar ningún arma y siempre llevar todas las que podamos a nuestra base cuando iniciamos una partida podremos encontrar algún cuchillo rodillo o sartén en la casa en la que exponemos Estas armas tendrán poco daño y poco alcance por lo que no será tan conveniente mantenerlas durante mucho tiempo pero siempre será mejor que solo pelear a mano una vez salgamos a explorar otras zonas como garajes y cobertizos encontraremos mejores armas como los martillos las barras de metal y tubos metálicos que serán un poco mejores en cuanto a daño y distancia y por último para encontrar las mejores del juego será necesario ir a los almacenes y fábricas donde encontraremos hachas picos palanquetas horquillas de jardín e incluso algún machete todas estas armas tienen las mejores estadísticas de daño distancia y durabilidad por lo que será siempre bueno tener la mayor cantidad posible almacenadas en nuestra base ya que tarde o temprano se terminarán rompiendo y precisamente para contrarrestar este deterioro tenemos los materiales de reparación estos materiales son cuatro principalmente la cinta americana la cinta adhesiva el pegamento y el pegamento para madera de estos cuatro materiales de reparación los mejores serán la cinta americana y el pegamento para madera ya que son los que mayor porcentaje de reparación otorgarán el pegamento de madera habrá que ocuparlo para reparar hachas y picos y entre mayor nivel de carpintería tengamos mayor será el porcentaje de reparación por otro lado la cinta americana será mejor ocuparla para reparar los machetes y hacer materiales y herramientas ya que hablamos de los almacenes y las fábricas pasemos con otros de los objetos que siempre deberemos de agarrar cuando vayamos a estos sitios y son los materiales y las herramientas estos objetos tienen cuatro propósitos principalesmente y son el mantenimiento el montaje el desmontaje y la construcción como herramientas útiles tendremos el martillo que aunque ya lo mencioné como un arma también servirá para poder ocupar la habilidad de carpintería la sierra o Sierra de jardín son muy útiles para la habilidad de trampas para cerrar troncos y para el desmontaje de muebles o estructuras de madera El destornillador que sirve para el desmontaje y creación de objetos electrónicos el desmontaje de estructuras de madera y para el mantenimiento de los vehículos la llave inglesa la llave de cruz y el gato los ocuparemos para darle mantenimiento a los vehículos con la habilidad de mecánica la llave para tubos nos servirá para poder desmontar lavabos y volverlos a colocar en otro sitio y así poderlos conectar con los recolectores de lluvia el soplete y la máscara de soldador nos servirán para poder ocupar las habilidades de metalistería Y darles mantenimiento a los vehículos y como última herramienta tenemos la herramienta de destrucción por excelencia que es la almadena con este objeto podremos destruir cualquier estructura y principalmente la podremos ocupar para acceder a algunos lugares importantes como los almacenes o las tiendas de armas por otro lado como materiales tendremos los clavos que los ocuparemos en la habilidad de carpintería trampas y pesca el alambre que sirve para las habilidades de trampas y pesca objetos de agricultura estos objetos Igualmente podremos encontrarlos en almacenes y fábricas y como su nombre lo dice son objetos que nos servirán para poder ocupar la habilidad de agricultura que la agricultura es la mejor forma de tener una fuente de alimentación duradera los objetos que entran en esta categoría son las herramientas para crear surcos que puede ser cualquier tipo de pala o una horquilla de jardín o asada las semillas que normalmente las encontraremos en paquetes de 50 semillas los aerosoles para crear aerosoles medicinales y la regadera de agua que servirá para poder mantener hidratadas a las plantas sin embargo podremos ocupar cualquier otro recipiente que pueda contener agua generador y bidón de gasolina otro de los aspectos más importantes a tratar en este juego es el corte de luz eléctrica por lo que será necesario ocupar otro objeto que nunca debemos de olvidar llevar a nuestra base y son los generadores eléctricos estos generadores los podremos encontrar principalmente en garajes y cobertizos y se necesitará gasolina para que puedan funcionar y para esto ocuparemos otro objeto más que son los bidones de gasolina Estos bidones son la forma más eficiente de transportar gasolina de un lugar a otro y los podremos encontrar en cobertizos gasolineras y en talleres mecánicos así podremos llenar de gasolina los generadores eléctricos y los tanques de gasolina de los vehículos Recuerden que cuando hay el corte de energía eléctrica las bombas de gasolina dejarán de funcionar por lo que hay que tener dos generadores a la mano uno para nuestra base y otro para colocarlo en alguna gasolinera cercana libros y revistas también hay que tomar en cuenta que para poder ocupar el generador deberemos de leer las revistas de generadores lo que nos llevará a los siguientes objetos que siempre debemos de luchar y son los libros y las revistas al leer los libros obtendremos diferentes multiplicadores de experiencia para cada una de las habilidades del juego pero siempre hay que tener un control de cuáles libros ya hemos llevado y cuáles no para evitar tener libros repetidos aun así habrá algunos libros que serán un poco más importantes que otros estos serán los libros de agricultura y carpintería ya que estas dos habilidades nos ayudarán a la supervivencia a largo plazo por otro lado las revistas nos servirán para saber algunos crafteos útiles y aprenderemos algunas habilidades especiales las revistas que más nos interesa tener son el manual de cómo usar generadores las guías de vehículos y las revistas de casa trampas y agricultura todos estos objetos de lectura podremos encontrarlos en los buzones de las casas las tiendas de libros los revisteros de las gasolineras las oficinas postales las librerías de las escuelas o en los libreros de cualquier clase mochilas y contenedores Y por último y no por eso menos importante hay un grupo de objetos que siempre será importante lutear y son las mochilas las mochilas son objetos que sirven como contenedores que podremos equipar en la espalda O en nuestras manos para así poder ampliar nuestro inventario todas las mochilas cuentan con dos estadísticas la capacidad de carga y la reducción de peso la capacidad de carga máxima simplemente es el máximo peso que puede llevar y la reducción de peso es el porcentaje Que hará que un objeto disminuya su peso esta reducción irá desde el 30% hasta el 87% dependiendo de la mochila las mochilas pueden encontrarse en varios lugares desde los armarios de las casas hasta equipada en algunos zombies pero algunos de los lugares donde podremos asegurar encontrar aunque sea una mochila escolar será Precisamente en las escuelas en esta misma categoría podremos incluir las bolsas de basura que cumplirán la misma función que cualquier mochila sin embargo solo las podremos equipar en alguna de las manos y su reducción de peso solo es del 20% pero su mayor importancia es como material para la creación de colectores de lluvia Así que siempre que veamos una de estas bolsas Será muy importante lutearla estas bolsas siempre estarán en papeleras o en cualquier contenedor de basura y bueno gente hasta aquí la guía de objetos que siempre debemos de lootear es una guía un poco más pequeña pero espero que les sirva para poder saber qué objetos son más importantes que otros también Déjenme en los comentarios si para ustedes olvidé mencionar algún objeto que es muy importante para lutear así siempre podremos ayudar a los nuevos jugadores que lleguen a ver el video recuerden dejar su like suscribirse y comentarme que les pareció el vídeo y de que otro tema les gustaría que hablara en el canal cuídense mucho nos vemos pronto Chau

</details>

---
---

<details><summary>UBICACIONES y SECRETOS del MOD RAVEN CREEK PROJECT ZOMBOIDUBICACIONES y SECRETOS del MOD RAVEN CREEK PROJECT ZOMBOID.txt</summary>

UBICACIONES y SECRETOS del MOD RAVEN CREEK | PROJECT ZOMBOID
---
https://www.youtube.com/watch?v=nYflN-aMzV4
---
hola fierecillas hoy os traigo un vídeo en el cual vamos a repasar todas las localizaciones interesantes de raven crit y sus rincones secretos o lo que hoy en día está de moda decir esther ex para quien esté perdido la ciudad de raven cree que es el mod de mapeado más popular de project zombie y es que realmente es muy currado estás sobradísimo como siempre os dejaré el enlace en el canal de mods guías y series de mi disco por si lo queréis descargar tengo intención de que esto se convierta en una serie en la cual vaya repasando ubicaciones importantes de mapeados de proyección voy así que si la idea te mola deja un like para ver si la cosa encaja pero espera espera te quiero recordar que el instant gaming puedes comprar videojuegos muy económicos y muy sabroso nes utiliza mi link que está aquí abajo en la descripción para apoyar el canal y sobre todo pues eso juegos juegos y juegos baratos primero ubicaremos la ciudad que está al suroeste del mapa vanilla este monte da la opción de hacer spawn allí mismo así que puedes jugar directamente en ella o de otra forma ir desde cualquier otro sitio y vas a esta ciudad tendrá que venir preparado ya que la entrada te va a poner cierto problemas sobre todo si quieres entrar con tu coche deberás destruir barricadas y vallas con una alma de na aunque si quieres entrar andando hay este camino alternativo por el lado del túnel aunque más adelante seguirás teniendo dificultades sin un alma de na así que te los recomiendo encarecidamente no vayas sin ella o spawn ya directamente en la ciudad la primera ubicación que os quiero mostrar es una especie de zona industrial que está justo a la entrada o salida de la ciudad vas a necesitar una almacena para entrar y te recomiendo que vengas con un buen nivel de carpintería ahora luego entenderás el porque tendrás varios garajes donde poder encontrar multitud de herramientas y materiales industriales a la vez en mi opinión estás jugando sobre todo en multiplayer parece un buen sitio para hacer una base ya que es enorme y está totalmente cerrada con alambres de espinos así que vuestra facción no podrá apretar de vehículos y cada uno tendrá un buen espacio para él en este garaje encontrarás un muro de madera los rompes y podrás acceder a estas estanterías y al piso de arriba y es que el truco está en que si construyes una escalera justo aquí podrás acceder a un contenedor al lavado igual a la fiesta del lute hermano otra ubicación interesante es el complejo médico convertido en base militar ya solo por lo ocurrido que está os aconsejo que vayáis y lo explorer jce es muy chulo en serio tendrás tres formas de acceder y te las voy a enseñar todas no te preocupes se puede acceder por la parte norte como veis te vas a encontrar un muro que siempre lo puedes reventar con la almacena pero si no vas por la derecha y saltas este muro así que ya estás dentro avanzas abres esta puerta continúas y vaya puerta bloqueada así que amigo almacena o almacena por aquí por otro lado si entras por el lado este es simplemente avanzar por esta calle y abrir la puerta pero por la parte sur siguiendo esta callejuela encontraremos un acceso que ya está abierto no tengo muy claro si el creador de este modo se le olvidó poner el muro allí aunque lo dudo o en realidad quería que se pudiera acceder por este rinconcito en este edificio grande lo que podremos encontrar principalmente son medicinas y algunas estanterías con libros típico que te encontrarías en un hospital en este otro pabellón también necesitaremos la almacena para acceder a los sitios más interesantes y es que si subes al segundo piso vas a encontrar una pequeña salita donde hay mucho armamento también te animo a que explores todo el pabellón entero porque hay salas un poco bizarras no os voy a spoiler pero es interesante parece que hicieran experimentos con los zombies en este otro punto de aquí vais a encontrar bastante luz hay varias casas donde podréis encontrar suministros muy interesantes y ya por último nos queda la zona esta que son un montón de barracones y tiendas al entrar siempre encontraréis ese típico armario lleno de armas y munición otra ubicación militarizada de rubén click está al sur esto es como una especie de control de paso pero está peta disc y model un militar y una vez más como siempre nuestra querida almádena nos abrirá el camino hacia el preciado luz esta base militar es grande así que te va a llevar bastante rato saquear la toda seguramente tendrás que pasar un par de noches por allí así que ves preparado sobre todo que no se te pasen los alijos de los barracones están abajo del todo la siguiente ubicación muchos no la conoceréis y es que se trata de la casa se cree de un superviviente en concreto hay dos ubicaciones la primera es en este garaje sólo es cuestión de entrar en él y fijarse detrás del todo en esa cosita que no acaba de encajar detrás de las cajas de madera pues nadie a reventarlo todo y te metes para adentro un no tiene más ya luego en el edificio que hay a la derecha del mismo garaje tendremos que subir hacia el segundo piso este grafiti nos alertará y justo tenemos que entrar en el apartamento que hay a su derecha pero vaya qué casualidad la puerta está atrancada por qué será pues nada los revientas todo y recto para dentro hasta el fondo igual a flipa la cantidad de luz sin necesidad de ir a una armería o una base militar donde hay muchos torneos venga venga me dirás que no este vídeo se merece tu pedazo de like us y kendall hermano dale luego como no tendremos que hablar de la prisión de raven creed no es un sitio al que vayamos a ir para lotear grandes cosas sino que sería más bien como reto de la misma forma quería saltear la prisión de rodwell aquí aparte de un montón de zombies con trajes naranjas así regiones de las prisiones yanquis y en el mismo edificio de la entrada subimos encontraremos una pequeña armería aparte de esto que yo sepa no hay nada más interesante pero vamos zombies van a poder matar todos los que quieras ahora os voy a mostrar un par de armerías donde podéis también sacar bastantes armas de fuego pues nada romper la persiana y para dentro no tiene más una pequeña armería la segunda armería se encuentra en esta ubicación entre el centro de la ciudad y la prisión bueno los del club del rifle no podréis negar que raven creeps proporciona mucho amor hermanos mucho amor y es que aquí hay más de uno que se pone tontito viendo estas vitrinas llenas de munición y armas no me lo negué igual que con las armerías en rebel creek hay dos comisarías la primera se encuentra en este punto y es un poco lioso encontrar los distintos sitios escondidos que tienen hay tres entradas la principal la lateral y una puerta trasera por la cual y una vez más no podrás entrar sin una almadén en esta comisaría yo he llegado a encontrar tres sitios distintos donde hay luz te muestro la primera ubicación desde la entrada trasera sígueme el camino hacia la segunda ubicación te lo muestro desde este sitio que creo que es bastante revelador y para ir a la tercera ubicación que yo creo que es la que más luz trae partiremos desde el hall de la comisaría la segunda comisaría está ubicada bastante en medio del meollo de raven creek justo en este punto en esta se representa como unos cuantos supervivientes la ocuparon al menos durante un tiempo la verdad que está chula hay bastantes barricadas y movidas pero yo os voy a enseñar el camino más fácil hacia la guindilla del pastel seguidme y lo siento mucho hermano pero me tengo que repetir una vez más sin alma de na tampoco podrás acceder a que la siguiente ubicación sería el puerto y su barco ubicado en la isla que hay al otro lado del río hacia el oeste pero primero os tengo que hablar un poco de cómo llegar hasta ahí porque es bastante enrevesado tienes dos opciones cruzarlo en coche lo que te obligará a ir abriendo mucho hueco y seguramente tener que apartar o destruir algún vehículo que otro o cruzarlo a pie que puede parecer una auténtica locura pero a veces los planes sencillos son los que salen mejor y si hermano el otro lado del puente también está cerrado así que tendrás que currárselo por dos una vez que lo hayas cruzados si es que lo has hecho a pie tienes que dirigirte a este parking aquí encontrarás varios vehículos si has llevado un bidón de gasolina mejor y si sabes hacer el puente mejor que mejor sea como sea procederá a seguir la carretera principal hasta llegar al peaje y nada no tiene pérdida llegas al puerto en él hay dos cositas interesantes la primera son los contenedores algunos los encontrarás vacíos pero ten cuidado porque otros los puedes encontrar pecados de zombis y otros queridos amigos tienen el caramelito que todos esperamos otro sitio interesante del puerto es el barco aquí aparte de tu querida almádena también tendrás que tener cierto nivel de carpintería porque vamos a levantar una escalera para acceder dentro de él ya que no hay ninguna otra manera rompemos y para adentro el barco la verdad es que está currado y además sería un muy buen sitio para hacerte una base porque tienes desde enfermería a habitaciones de todo por donde hemos entrado si giras la mano izquierda primero y luego a mano derecha encontrarás un alma muy curioso pero es que en estas cajas querido amigo no hay herramientas sino que hay vaya munición para un ejército de chavales pero es que este barco también tiene sus bromitas porque si te caes aquí y justo no llevas la almacena encima querido amigo no vas a salir nunca y no te olvides subir arriba del todo no tiene pérdida para sitio the raven creek que quiero destacar es una especie de campamento que se han montado puedes entrar por la puerta principal o colarte saltando la valla por detrás este sitio está muy currado a nivel de ambientación pero es que si consigues limpiar lo tendrás incluso algún arma de fuego que 'el lute' ar hay víveres y electrodomésticos y muebles para liberar habilidades lo único malo que le veo es que está muy en el centro de la ciudad y el spam en dificultades altas puede ser una tortura mientras te muestro la base ya sólo me queda agradecer te que has llegado hasta aquí dice mucho de ti recordarte que le das un pedazo de like a este vídeo que te suscribas si quieres seguir viendo mi contenido y sobre todo que te pases a saludar por tweets es donde estamos todas las tardes y de risas y cachondeo un abrazo y hasta el siguiente vídeo chao

</details>

---

