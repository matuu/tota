# tota engine and game settings
DEFAULT_COLOR = 'white'

CREEP_LIFE = 100
TREE_LIFE = 200
HERO_LIFE = 100
TOWER_LIFE = 500
ANCIENT_LIFE = 1000

MOVE_DISTANCE = 1

HERO_ATTACK_DISTANCE = 1.5
HERO_ATTACK_BASE_DAMAGE = (10, 15)
HERO_ATTACK_LEVEL_MULTIPLIER = 0.2

HERO_RESPAWN_COOLDOWN = 30
HERO_HEALTH_LEVEL_MULTIPLIER = 0.2

TOWER_ATTACK_DISTANCE = 3
TOWER_ATTACK_BASE_DAMAGE = (20, 30)

CREEP_ATTACK_DISTANCE = 1.5
CREEP_ATTACK_BASE_DAMAGE = (10, 15)
CREEP_AGGRO_DISTANCE = 5
CREEP_WAVE_COOLDOWN = 50
CREEP_WAVE_SIZE = 4

HEAL_DISTANCE = 5
HEAL_BASE_HEALING = (20, 30)
HEAL_LEVEL_MULTIPLIER = 0.2
HEAL_RADIUS = 2
HEAL_COOLDOWN = 20

FIREBALL_DISTANCE = 5
FIREBALL_BASE_DAMAGE = (20, 30)
FIREBALL_LEVEL_MULTIPLIER = 0.2
FIREBALL_RADIUS = 2
FIREBALL_COOLDOWN = 20

STUN_DISTANCE = 3
STUN_COOLDOWN = 20
STUN_DURATION = 5

TEAM_RADIANT = 'radiant'
TEAM_DIRE = 'dire'
TEAM_NEUTRAL = 'neutral'

XP_DISTANCE = 10
XP_CREEP_DEAD = 10
XP_HERO_DEAD = 100
XP_TOWER_DEAD = 200
XP_TO_LEVEL = 100

TEAM_COLORS = {
    TEAM_RADIANT: 'blue',
    TEAM_DIRE: 'red',
    TEAM_NEUTRAL: 'green',
}

ENEMY_TEAMS = {
    TEAM_RADIANT: TEAM_DIRE,
    TEAM_DIRE: TEAM_RADIANT,
    TEAM_NEUTRAL: None,
}
