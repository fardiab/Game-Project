from play_game_interface import introduction
from log_in_and_register import login
from log_in_and_register import register
from play_game_interface import interface, map
from customization import character, weapon
from missions import mission
from setting import video, audio

print(introduction.Introduction())
print("----- Register -----")

fardi = register.User(input("Enter an username: "), input("Enter E-mail: ") ,input("Enter a password: "))

print(fardi.to_json())
print("----- Log in -----")

fardi1 = login.LogIn(input("Enter an username: "), input("Enter a password: "))

print(fardi1)

match = interface.Match()
menu = interface.Menu()
score = interface.Score()
fate = interface.FateOfTheGame()
coin = interface.Coin()
customization = interface.Customization()
armor = character.Armor()
# weapon = weapon.Weapon()
m4a1 = weapon.M4A1()
ak_47 = weapon.AK_47()
lmg = weapon.LightMachineGun()
deagle = weapon.DesertEagle()
MISSION = mission.Mission()
setting = video.Setting()
VIDEO = video.Video()
audio = audio.Audio()
advance_video = video.AdvanceVideo()


while True:
    print(interface.Menu().show_menu())
    input1 = int(input("Enter: "))
    while input1 == 1:
        print(match.show_menu())
        input1 = int(input("Enter: "))
        if input1 == 1:
            print(match.team_death_match())

        elif input1 == 2:
            print(match.death_match())

        elif input1 == 3:
            print(match.team_catch_flag())

        elif input1 == 4:
            print(match.kill_of_the_match())

        print(map.Map().show_maps())
        input1 = int(input("Enter: "))

        if input1 == 1:
            print(map.Map().join())

        elif input1 == 2:
            print(map.Map("Nuken").join())

        elif input1 == 3:
            print(map.Map("Containment").join())

        elif input1 == 4:
            print(map.Map("Deadlock").join())

        elif input1 == 5:
            print(map.Map("Decay").join())

        elif input1 == 6:
            print(map.Map("Vertigo").join())

        elif input1 == 7:
            print(map.Map("Shelter").join()) 

        print(match.choose_team())
        input1 = int(input("Enter: "))

        if input1 == 1:
            print(match.join_team(input1))

        elif input1 == 2:
            print(match.join_team(input1))

        print(score.kill_death_score(4, 7))
        print("------ Game Over ------")
        print(fate.win())
        print("------    Coin    ------")
        print(coin.collect_coins(4, 7))
        break

    while input1 == 2:
        print(customization)
        input1 = int(input("Enter: "))
        if input1 == 1:
            print(armor.your_armor())
            print(armor.get_info())
            print(armor.choice())
            input1 = int(input("Enter: "))
            if input1 == 1:
                input1 = input("Enter Headset: ")
                print(armor.set_head(input1))

            elif input1 == 2:
                input1 = input("Enter Bodyset: ")
                print(armor.set_body(input1))

            elif input1 == 3:
                input1 = input("Enter Bootset: ")
                print(armor.set_boot(input1))
        
        elif input1 == 2:
            print(weapon.WeaponList())
            input1 = int(input("Enter: "))
            if input1 == 1:
                print(m4a1.muzzle_part())
                print(m4a1.barrel_part())
                print(m4a1.scope_part())
                print(m4a1.magazine_part())
                print(m4a1.stock_part())
                print(m4a1.change_parts())
                input1 = int(input("Enter: "))
                print(m4a1.get_info())
                if input1 == 1:
                    input1 = input("Enter part: ")
                    print(m4a1.restore_M4A1_muzzle(input1))

                elif input1 == 2:
                    input1 = input("Enter part: ")
                    print(m4a1.restore_M4A1_barrel(input1))

                elif input1 == 3:
                    input1 = input("Enter part: ")
                    print(m4a1.restore_M4A1_scope(input1))

                elif input1 == 4:
                    input1 = input("Enter part: ")
                    print(m4a1.restore_M4A1_magazine(input1))

                elif input1 == 5:
                    input1 = input("Enter part: ")
                    print(m4a1.restore_M4A1_stock(input1))

            elif input1 == 2:
                print(ak_47.muzzle_part())
                print(ak_47.barrel_part())
                print(ak_47.scope_part())
                print(ak_47.magazine_part())
                print(ak_47.stock_part())
                print(ak_47.change_parts())
                input1 = int(input("Enter: "))
                print(ak_47.get_info())
                if input1 == 1:
                    input1 = input("Enter part: ")
                    print(ak_47.restore_AK_47_muzzle(input1))

                elif input1 == 2:
                    input1 = input("Enter part: ")
                    print(ak_47.restore_AK_47_barrel(input1))

                elif input1 == 3:
                    input1 = input("Enter part: ")
                    print(ak_47.restore_AK_47_scope(input1))

                elif input1 == 4:
                    input1 = input("Enter part: ")
                    print(ak_47.restore_AK_47_magazine(input1))

                elif input1 == 5:
                    input1 = input("Enter part: ")
                    print(ak_47.restore_AK_47_stock(input1))

            elif input1 == 3:
                print(lmg.muzzle_part())
                print(lmg.barrel_part())
                print(lmg.scope_part())
                print(lmg.magazine_part())
                print(lmg.change_parts())
                input1 = int(input("Enter: "))
                print(lmg.get_info())
                if input1 == 1:
                    input1 = input("Enter part: ")
                    print(lmg.restore_Light_Machine_Gun_muzzle(input1))

                elif input1 == 2:
                    input1 = input("Enter part: ")
                    print(lmg.restore_Light_Machine_Gun_barrel(input1))

                elif input1 == 3:
                    input1 = input("Enter part: ")
                    print(lmg.restore_Light_Machine_Gun_scope(input1))

                elif input1 == 4:
                    input1 = input("Enter part: ")
                    print(lmg.restore_Light_Machine_Gun_magazine(input1))

            elif input1 == 4:
                print(deagle.muzzle_part())
                print(deagle.scope_part())
                print(deagle.magazine_part())
                print(deagle.change_parts())
                input1 = int(input("Enter: "))
                print(deagle.get_info())
                if input1 == 1:
                    input1 = input("Enter part: ")
                    print(deagle.restore_desert_eagle_muzzle(input1))

                elif input1 == 2:
                    input1 = input("Enter part: ")
                    print(deagle.restore_desert_eagle_scope(input1))

                elif input1 == 3:
                    input1 = input("Enter part: ")
                    print(deagle.restore_desert_eagle_magazine(input1))
    
    while input1 == 3:
        print(MISSION.show_mission())
        break

    while input1 == 4:
        print(setting)
        input1 = int(input("Enter: "))
        
        if input1 == 1:
            print(VIDEO.get_resolution())
            print(VIDEO.get_brightness())
            print(VIDEO.get_window_mode())
            print(VIDEO.get_texture_quality())
            print(VIDEO.change_part())
            input1 = int(input("Enter: "))
            if input1 == 1:
                input1 = input("Change Resolution: ")
                print(VIDEO.set_resolution(input1))

            elif input1 == 2:
                input1 = input("Change Brightness: ")
                print(VIDEO.set_brightness(input1))
            
            elif input1 == 3:
                input1 = input("Change Window Mode: ")
                print(VIDEO.set_window_mode(input1))

            elif input1 == 4:
                input1 = input("Change Texture Quality: ")
                print(VIDEO.set_texture_quality(input1))

        elif input1 == 2:
            print(audio.get_audio_level())
            print(audio)
            input1 = int(input("Enter: "))
            if input1 == 1:
                input1 = int(input("Change Audio Level: "))
                print(audio.set_audio_level(input1))
            
            elif input1 == 2:
                break
        
        elif input1 == 3:
            print(advance_video.get_advance_resolution())
            print(advance_video.get_dynamic_shadows())
            print(advance_video.get_dynamic_lights())
            print(advance_video.get_directx11())
            print(advance_video.change_part())
            input1 = int(input("Enter: "))
            if input1 == 1:
                input1 = input("Change Dynamic Shadow: ")
                print(advance_video.set_dynamic_shadows(input1))
            
            elif input1 == 2:
                input1 = input("Change Dynamic Light: ")
                print(advance_video.set_dynamic_lights(input1))

            elif input1 == 3:
                input1 = input("Change Directx11: ")
                print(advance_video.set_directx11(input1))

            elif input1 == 4:
                break

    while input1 == 5:
        print("-----------  You Exit -----------")
        break
    break
            



