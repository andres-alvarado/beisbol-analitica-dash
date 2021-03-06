# Custom dependencies
import commons.data as d
import commons.functions as f

# List of Values.
object_specs = {
    "container_control": {
        "header": "Centro de Control",
        "children": [],
        "object_type": "container",
    },
    "container_winPercentage": {
        "header": "Carreras y Porcentajes de Victoria",
        "children": [],
        "object_type": "container",
    },
    "container_games": {
        "header": "Partidos",
        "children": [],
        "object_type": "container",
    },
    "container_games_row1": {
        "children": [],
        "object_type": "row",
        "container": "container_games",
    },
    "container_games_row2": {
        "children": [],
        "object_type": "row",
        "container": "container_games",
    },
    "container_batting": {
        "header": "Estadisticas de Bateo",
        "children": [],
        "object_type": "container",
    },
    "container_batting_row1": {
        "children": [],
        "object_type": "row",
        "container": "container_batting",
    },
    "container_batting_row2": {
        "children": [],
        "object_type": "row",
        "container": "container_batting",
    },
    "container_batting_row3": {
        "children": [],
        "object_type": "row",
        "container": "container_batting",
    },
    "lov_season": {
        "dataset_name": "agg_team_performance_stats",
        "object_type": "lov",
        "id": "lov_season",
        "label_col": "seasonId",
        "value_col": "seasonId",
        "P": "Temporada",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": 2017,
        "clearable": False,
        "placeholder": "Selecciona una Temporada",
        "multi": False,
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
        "searchable" : False
    },
    "lov_majorLeague": {
        "dataset_name": "agg_team_performance_stats",
        "object_type": "lov",
        "id": "lov_majorLeague",
        "label_col": "majorLeague",
        "value_col": "majorLeagueId",
        "P": "Liga",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": 125,
        "clearable": False,
        "placeholder": "Selecciona una Liga",
        "multi": False,
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "callback_output": None,
        "callback_input": None,
        "container": "container_control",
        "searchable" : False
    },
    "lov_team": {
        "dataset_name": "agg_team_performance_stats",
        "object_type": "lov",
        "id": "lov_team",
        "label_col": "teamName",
        "value_col": "teamId",
        "P": "Equipo",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": 562,
        "clearable": False,
        "placeholder": "Selecciona un Equipo",
        "multi": False,
        "container": "container_control",
        "searchable" : False,
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "gameType2": "RS",
            "groupingDescription": "MAJORLEAGUEID_SEASONID_GAMETYPE2_TEAMID",
        },
        "callback_output": [
            {"component_id": "lov_team", "component_property": "options"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
        ],
    },
    "lov_teamType": {
        "dataset_name": "teamType",
        "object_type": "lov",
        "id": "lov_teamType",
        "label_col": "label",
        "value_col": "value",
        "P": "Local/Visitante",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": "",
        "clearable": False,
        "placeholder": "Selecciona un Valor",
        "multi": False,
        "default_filters": None,
        "callback_output": None,
        "callback_input": None,
        "searchable" : False,
        "container": "container_control",
        "callback_output": [
            {"component_id": "lov_teamType", "component_property": "options"}
        ],
    },
    "lov_gameType2": {
        "dataset_name": "gameType2",
        "object_type": "lov",
        "id": "lov_gameType2",
        "label_col": "label",
        "value_col": "value",
        "P": "Tipo de Partido",
        "style": {"text-align": "center", "font-size": "12px", "width": "100%"},
        "value": "RS",
        "clearable": False,
        "placeholder": "Selecciona un Valor",
        "multi": False,
        "default_filters": None,
        "callback_output": None,
        "callback_input": None,
        "searchable" : False,
        "container": "container_control",
        "callback_output": [
            {"component_id": "lov_gameType2", "component_property": "options"}
        ],
    },
    "fig_winPercentage": {
        "dataset_name": "agg_team_performance_stats",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_winPercentage",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
        },
        "fig_type": "line",
        "fig_specs": {
            "melt_by": ["gameDate"],
            "x": "gameDate",
            "metrics": ["W%", "PyExp"],
            "title": "Porcentaje de Victoria",
            "color": "metric",
            "color_discrete_map": {},
            "labels": {
                "metrica": "Metrica",
                "value": "Total",
                "gameDate": "Fecha",
                "teamName": "Equipo",
            },
            "showlegend": True,
            "height": 350,
            "orientation": "h",
        },
        "container": "container_winPercentage",
        "callback_output": [
            {"component_id": "fig_winPercentage", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_wins_losses": {
        "dataset_name": "agg_team_performance_stats",
        "container": "container_winPercentage",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_wins_losses",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
        },
        "fig_type": "line",
        "fig_specs": {
            "melt_by": ["gameDate"],
            "x": "gameDate",
            "metrics": ["W", "L"],
            "title": "Victorias y Derrotas",
            "color": "teamName",
            "color_discrete_map": {},
            "labels": {
                "metrica": "Metrica",
                "value": "Total",
                "gameDate": "Fecha",
                "teamName": "Equipo",
            },
            "showlegend": True,
            "height": 350,
            "orientation": "h",
        },
        "callback_output": [
            {"component_id": "fig_wins_losses", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_runDifferential": {
        "dataset_name": "agg_team_performance_stats",
        "container": "container_winPercentage",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_runDifferential",
        "default_filters": {
            "aggregationType": "CUMULATIVE",
        },
        "fig_type": "line",
        "fig_specs": {
            "melt_by": ["gameDate"],
            "x": "gameDate",
            "metrics": ["RS-RA", "RA", "R"],
            "title": "Carreras",
            "color": "metric",
            "color_discrete_map": {},
            "labels": {
                "metrica": "Metrica",
                "value": "Total",
                "gameDate": "Fecha",
                "teamName": "Equipo",
            },
            "showlegend": True,
            "height": 350,
            "orientation": "h",
        },
        "callback_output": [
            {"component_id": "fig_runDifferential", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_games": {
        "dataset_name": "games",
        "container": "container_games_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_games",
        "default_filters": {},
        "fig_type": "bar",
        "fig_specs": {
            "x": "gameDate",
            "y": "runDifference",
            "title": "Resultados de Partidos",
            "color": "resultado",
            "color_discrete_map": {"Ganado": "#00cc96", "Perdido": "#ee563b"},
            "labels": {
                "resultado": "Resultado",
                "runDifference": "Diferencia de Carreras",
                "gameDate": "Fecha",
            },
            "showlegend": True,
            "height": 350,
            "orientation": "v",
        },
        "callback_output": [
            {"component_id": "fig_games", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_attendance": {
        "dataset_name": "games",
        "container": "container_games_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_attendance",
        "default_filters": {},
        "fig_type": "bar",
        "fig_specs": {
            "x": "gameDate",
            "y": "attendance",
            "title": "Asistencia del Publico",
            "color": None,
            "color_discrete_map": {},
            "labels": {
                "attendance": "Asistencia",
                "gameDate": "Fecha",
            },
            "showlegend": False,
            "height": 350,
            "orientation": "v",
        },
        "callback_output": [
            {"component_id": "fig_attendance", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_hit_distribution": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_hit_distribution",
        "fig_type": "pie",
        "default_filters": {
            "aggregationType": "AGGREGATED",
        },
        "fig_specs": {
            "title": "Distribucion de Hits",
            "melt_by": ["teamName"],
            "metrics": [
                "X1B",
                "X2B",
                "X3B",
                "HR",
            ],
            "labels": {
                "metric": "Metrica",
                "value": "Total",
            },
            "showlegend": True,
            "height": 280,
            "orientation": "v",
        },
        "callback_output": [
            {"component_id": "fig_hit_distribution", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_plate_appearance_distribution": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_plate_appearance_distribution",
        "fig_type": "pie",
        "default_filters": {
            "aggregationType": "AGGREGATED",
        },
        "fig_specs": {
            "title": "Distribucion de Apariciones al Plato",
            "melt_by": ["teamName"],
            "metrics": ["SO", "H", "BB", "HBP"],
            "labels": {
                "metric": "Metrica",
                "value": "Total",
            },
            "showlegend": True,
            "height": 280,
            "orientation": "v",
        },
        "callback_output": [
            {
                "component_id": "fig_plate_appearance_distribution",
                "component_property": "figure",
            }
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_fb_ab_distribution": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_fb_ab_distribution",
        "fig_type": "pie",
        "default_filters": {
            "aggregationType": "AGGREGATED",
        },
        "fig_specs": {
            "title": "Distribucion de FlyBalls y Groundballs",
            "melt_by": ["teamName"],
            "metrics": [
                "PU",
                "GB",
                "LD",
                "FB",
            ],
            "labels": {
                "metric": "Metrica",
                "value": "Total",
            },
            "showlegend": True,
            "height": 280,
            "orientation": "v",
        },
        "callback_output": [
            {"component_id": "fig_fb_ab_distribution", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    }, "fig_lob_distribution": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_lob_distribution",
        "fig_type": "pie",
        "default_filters": {
            "aggregationType": "AGGREGATED",
        },
        "fig_specs": {
            "title": "Distribucion de Carreras",
            "melt_by": ["teamName"],
            "metrics": [
                "RBI",
                "LOB"
            ],
            "labels": {
                "metric": "Metrica",
                "value": "Total",
            },
            "showlegend": True,
            "height": 240,
            "orientation": "v",
        },
        "callback_output": [
            {"component_id": "fig_lob_distribution", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_sb_distribution": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row1",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_sb_distribution",
        "fig_type": "pie",
        "default_filters": {
            "aggregationType": "AGGREGATED",
        },
        "fig_specs": {
            "title": "Distribucion de Robo de Base",
            "melt_by": ["teamName"],
            "metrics": [
                "SB",
                "CS"
            ],
            "labels": {
                "metric": "Metrica",
                "value": "Total",
            },
            "showlegend": True,
            "height": 260,
            "orientation": "v",
        },
        "callback_output": [
            {"component_id": "fig_sb_distribution", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "table_games": {
        "dataset_name": "games",
        "container": "container_games_row2",
        "object_type": "table",
        "fig_type": "table",
        "id": "table_games",
        "fig": {},
        "fig_specs": {
            "id": "table_games",
            "sort_action": "native",
            "style_cell": {
                "fontSize": 11,
                "font-family": "sans-serif",
                "textAlign": "center",
                "vertical-align": "top",
            },
            "page_size": 7,
            "columns": {
                "Fecha": {"id": "gameDate", "type": "text", "presentation": "text"},
                "Boxscore": {
                    "id": "boxscoreUrl",
                    "type": "any",
                    "presentation": "markdown",
                },
                "Jugada a Jugada": {
                    "id": "playByPlayUrl",
                    "type": "any",
                    "presentation": "markdown",
                },
                "Estadio": {"id": "venueName", "type": "text", "presentation": "text"},
                "Equipo Local": {
                    "id": "homeTeamName",
                    "type": "text",
                    "presentation": "text",
                },
                "Marcador": {
                    "id": "resultadoCarreras",
                    "type": "text",
                    "presentation": "text",
                },
                "Equipo Visitante": {
                    "id": "awayTeamName",
                    "type": "text",
                    "presentation": "text",
                },
                "Resultado": {
                    "id": "resultado",
                    "type": "text",
                    "presentation": "text",
                },
                "Asistencia": {
                    "id": "attendance",
                    "type": "text",
                    "presentation": "text",
                },
                "Doble Juego": {
                    "id": "doubleHeader",
                    "type": "text",
                    "presentation": "text",
                },
                "Dia/Noche": {"id": "dayNight", "type": "text", "presentation": "text"},
                "Clima": {"id": "weather", "type": "text", "presentation": "text"},
            },
            "style_table": {"width": "100%"},
            "fill_width": False,
            "css": [{"selector": "table", "rule": "width: 100%;"}],
        },
        "default_filters": {},
        # "container": "container_games",
        "callback_output": [
            {"component_id": "table_games", "component_property": "data"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "table_player_batting_stats": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row2",
        "object_type": "table",
        "fig_type": "table",
        "id": "table_player_batting_stats",
        "fig": {},
        "fig_specs": {
            "id": "table_player_batting_stats",
            "sort_action": "native",
            "style_cell": {
                "fontSize": 11,
                "font-family": "sans-serif",
                "textAlign": "center",
                "vertical-align": "top",
            },
            "page_size": 7,
            "columns": {
                "Jugador": {
                    "id": "playerName",
                    "type": "text",
                    "presentation": "text",
                },
               "G": {
                    "id": "G",
                    "type": "text",
                    "presentation": "text",
                },
               "PA": {
                    "id": "PA",
                    "type": "text",
                    "presentation": "text",
                },
               "AB": {
                    "id": "AB",
                    "type": "text",
                    "presentation": "text",
                },
               "R": {
                    "id": "R",
                    "type": "text",
                    "presentation": "text",
                },
               "H": {
                    "id": "H",
                    "type": "text",
                    "presentation": "text",
                },
               "X1B": {
                    "id": "X1B",
                    "type": "text",
                    "presentation": "text",
                },
               "X2B": {
                    "id": "X2B",
                    "type": "text",
                    "presentation": "text",
                },
               "X3B": {
                    "id": "X3B",
                    "type": "text",
                    "presentation": "text",
                },
               "HR": {
                    "id": "HR",
                    "type": "text",
                    "presentation": "text",
                },
               "RBI": {
                    "id": "RBI",
                    "type": "text",
                    "presentation": "text",
                },
               "SB": {
                    "id": "SB",
                    "type": "text",
                    "presentation": "text",
                },
               "CS": {
                    "id": "CS",
                    "type": "text",
                    "presentation": "text",
                },
               "UBB": {
                    "id": "UBB",
                    "type": "text",
                    "presentation": "text",
                },
               "IBB": {
                    "id": "IBB",
                    "type": "text",
                    "presentation": "text",
                },
               "SO": {
                    "id": "SO",
                    "type": "text",
                    "presentation": "text",
                },
               "BA": {
                    "id": "BA",
                    "type": "text",
                    "presentation": "text",
                },
               "OBP": {
                    "id": "OBP",
                    "type": "text",
                    "presentation": "text",
                },
               "SLG": {
                    "id": "SLG",
                    "type": "text",
                    "presentation": "text",
                },
               "OPS": {
                    "id": "OPS",
                    "type": "text",
                    "presentation": "text",
                },
               "TB": {
                    "id": "TB",
                    "type": "text",
                    "presentation": "text",
                },
               "GDP": {
                    "id": "GDP",
                    "type": "text",
                    "presentation": "text",
                },
               "HBP": {
                    "id": "HBP",
                    "type": "text",
                    "presentation": "text",
                },
               "SH": {
                    "id": "SH",
                    "type": "text",
                    "presentation": "text",
                },
               "SF": {
                    "id": "SF",
                    "type": "text",
                    "presentation": "text",
                },
            },
            "style_table": {"width": "100%"},
            "fill_width": False,
            "css": [{"selector": "table", "rule": "width: 100%;"}],
        },
        "default_filters": {
            "aggregationType": "AGGREGATED",
            "playerId": "dummy",
        },
        "callback_output": [
            {"component_id": "table_player_batting_stats", "component_property": "data"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
    "fig_contour_hm": {
        "dataset_name": "agg_batting_stats",
        "container": "container_batting_row3",
        "config": {"displayModeBar": False, "responsive": True},
        "fig": {},
        "object_type": "fig",
        "id": "fig_contour_hm",
        "fig_type": "contour_heatmap",

        "default_filters": {
            "aggregationType": "AGGREGATED",
        },
        "fig_specs": {
            "title": "Distribucion de Pelotas Puestas en Juego",
            "melt_by": [],
            "metrics": [],
            "labels":  {},
            "showlegend": False,
            "height": 350,
            "orientation": "v",
        }, "callback_output": [
            {"component_id": "fig_contour_hm", "component_property": "figure"}
        ],
        "callback_input": [
            {
                "component_id": "lov_majorLeague",
                "component_property": "value",
                "filter_col": "majorLeagueId",
            },
            {
                "component_id": "lov_season",
                "component_property": "value",
                "filter_col": "seasonId",
            },
            {
                "component_id": "lov_team",
                "component_property": "value",
                "filter_col": "teamId",
            },
            {
                "component_id": "lov_teamType",
                "component_property": "value",
                "filter_col": "teamType",
            },
            {
                "component_id": "lov_gameType2",
                "component_property": "value",
                "filter_col": "gameType2",
            },
        ],
    },
}

# Set the dataset and options spec. Abstract this
for (obj, specs) in object_specs.items():

    # Set lov specs
    if specs["object_type"] == "lov":
        df = f.filter_df(
            dataset_name=specs["dataset_name"],
            filter_cols=specs["default_filters"],
            default_filters=specs["default_filters"],
        )
        object_specs[obj]["options"] = f.create_list_of_values(
            df=df,
            label_col=specs["label_col"],
            value_col=specs["value_col"],
        )
