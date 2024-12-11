from agency_swarm.tools import BaseTool
from pydantic import Field
from typing import Dict, List, Optional
import json

class InterfaceDesigner(BaseTool):
    """
    A tool for designing user interfaces, visual components,
    and design systems.
    """
    
    design_spec: Dict = Field(
        ...,
        description="Design specifications including visual requirements, brand guidelines, and component needs"
    )
    
    design_type: str = Field(
        ...,
        description="Type of design needed: 'visual', 'components', 'system', or 'prototype'"
    )
    
    platform: Optional[str] = Field(
        "web",
        description="Target platform: 'web', 'mobile', or 'desktop'"
    )

    def run(self) -> str:
        """
        Designs user interfaces based on the specified parameters.
        """
        if self.design_type == "visual":
            return self._design_visual_style()
        elif self.design_type == "components":
            return self._design_components()
        elif self.design_type == "system":
            return self._design_system()
        elif self.design_type == "prototype":
            return self._create_prototype()
        else:
            return "Invalid design type specified"

    def _design_visual_style(self) -> str:
        style = {
            "color_palette": self._define_color_palette(),
            "typography": self._define_typography(),
            "spacing": self._define_spacing_system(),
            "imagery": self._define_imagery_style(),
            "iconography": self._define_iconography()
        }
        
        return json.dumps(style, indent=2)

    def _design_components(self) -> str:
        components = {
            "atomic_elements": self._design_atomic_elements(),
            "molecules": self._design_molecules(),
            "organisms": self._design_organisms(),
            "templates": self._design_templates(),
            "documentation": self._create_component_documentation()
        }
        
        return json.dumps(components, indent=2)

    def _design_system(self) -> str:
        system = {
            "foundations": self._define_foundations(),
            "components": self._define_component_library(),
            "patterns": self._define_design_patterns(),
            "guidelines": self._create_guidelines(),
            "resources": self._create_design_resources()
        }
        
        return json.dumps(system, indent=2)

    def _create_prototype(self) -> str:
        prototype = {
            "screens": self._design_screens(),
            "interactions": self._define_interactions(),
            "animations": self._define_animations(),
            "assets": self._prepare_assets(),
            "specifications": self._create_specifications()
        }
        
        return json.dumps(prototype, indent=2)

    def _define_color_palette(self) -> Dict:
        return {
            "primary": {
                "main": "#007AFF",
                "light": "#4DA3FF",
                "dark": "#0055B3"
            },
            "secondary": {
                "main": "#00C853",
                "light": "#4CDF80",
                "dark": "#008C3A"
            },
            "neutral": {
                "white": "#FFFFFF",
                "gray100": "#F5F5F5",
                "gray200": "#EEEEEE",
                "gray300": "#E0E0E0",
                "gray400": "#BDBDBD",
                "gray500": "#9E9E9E",
                "gray600": "#757575",
                "gray700": "#616161",
                "gray800": "#424242",
                "gray900": "#212121",
                "black": "#000000"
            },
            "feedback": {
                "success": "#00C853",
                "warning": "#FFB300",
                "error": "#D32F2F",
                "info": "#0288D1"
            }
        }

    def _define_typography(self) -> Dict:
        return {
            "font_families": {
                "primary": "Inter",
                "secondary": "Roboto",
                "monospace": "Source Code Pro"
            },
            "scale": {
                "h1": {
                    "size": "2.5rem",
                    "weight": "700",
                    "line_height": "1.2"
                },
                "h2": {
                    "size": "2rem",
                    "weight": "700",
                    "line_height": "1.25"
                },
                "h3": {
                    "size": "1.75rem",
                    "weight": "600",
                    "line_height": "1.3"
                },
                "body1": {
                    "size": "1rem",
                    "weight": "400",
                    "line_height": "1.5"
                },
                "body2": {
                    "size": "0.875rem",
                    "weight": "400",
                    "line_height": "1.5"
                },
                "caption": {
                    "size": "0.75rem",
                    "weight": "400",
                    "line_height": "1.4"
                }
            }
        }

    def _define_spacing_system(self) -> Dict:
        return {
            "base": "4px",
            "scale": {
                "xs": "4px",
                "sm": "8px",
                "md": "16px",
                "lg": "24px",
                "xl": "32px",
                "xxl": "48px"
            },
            "layout": {
                "container": "1200px",
                "gutter": "24px",
                "column": "72px"
            }
        }

    def _define_imagery_style(self) -> Dict:
        return {
            "photography": {
                "style": "Modern and clean",
                "treatment": "Natural colors",
                "composition": "Rule of thirds"
            },
            "illustrations": {
                "style": "Geometric and minimal",
                "colors": "Brand colors",
                "usage": "Feature highlights"
            }
        }

    def _define_iconography(self) -> Dict:
        return {
            "style": {
                "type": "Line icons",
                "weight": "2px",
                "corners": "Rounded",
                "size_grid": "24x24px"
            },
            "sets": {
                "navigation": ["home", "search", "menu"],
                "actions": ["add", "edit", "delete"],
                "status": ["success", "warning", "error"]
            }
        }

    def _design_atomic_elements(self) -> Dict:
        return {
            "buttons": {
                "primary": {
                    "background": "primary.main",
                    "text": "white",
                    "padding": "12px 24px",
                    "border_radius": "4px"
                },
                "secondary": {
                    "background": "transparent",
                    "text": "primary.main",
                    "border": "1px solid primary.main",
                    "padding": "12px 24px"
                }
            },
            "inputs": {
                "text": {
                    "height": "40px",
                    "padding": "8px 12px",
                    "border": "1px solid gray300"
                },
                "select": {
                    "height": "40px",
                    "padding": "8px 12px",
                    "border": "1px solid gray300"
                }
            }
        }

    def _design_molecules(self) -> Dict:
        return {
            "form_fields": {
                "text_field": {
                    "label": "Above input",
                    "helper_text": "Below input",
                    "error_state": True
                },
                "search_field": {
                    "icon": "Left aligned",
                    "clear_button": True,
                    "autocomplete": True
                }
            },
            "cards": {
                "basic": {
                    "padding": "16px",
                    "border_radius": "8px",
                    "shadow": "0 2px 4px rgba(0,0,0,0.1)"
                },
                "interactive": {
                    "hover_state": True,
                    "click_state": True,
                    "transition": "0.2s ease"
                }
            }
        }

    def _design_organisms(self) -> Dict:
        return {
            "navigation": {
                "header": {
                    "height": "64px",
                    "layout": "Flex between",
                    "components": ["Logo", "Nav Links", "Actions"]
                },
                "sidebar": {
                    "width": "240px",
                    "layout": "Flex column",
                    "components": ["User Info", "Nav Menu", "Footer"]
                }
            },
            "forms": {
                "login": {
                    "fields": ["Email", "Password"],
                    "actions": ["Submit", "Forgot Password"],
                    "validation": True
                },
                "registration": {
                    "fields": ["Name", "Email", "Password"],
                    "terms": True,
                    "validation": True
                }
            }
        }

    def _design_templates(self) -> Dict:
        return {
            "page_layouts": {
                "dashboard": {
                    "header": "Fixed top",
                    "sidebar": "Fixed left",
                    "content": "Scrollable"
                },
                "article": {
                    "header": "Sticky",
                    "content": "Centered container",
                    "footer": "Sticky bottom"
                }
            },
            "responsive_behavior": {
                "breakpoints": {
                    "mobile": "< 768px",
                    "tablet": "768px - 1024px",
                    "desktop": "> 1024px"
                },
                "adaptations": {
                    "navigation": "Mobile menu",
                    "layout": "Stack on mobile"
                }
            }
        }

    def _create_component_documentation(self) -> Dict:
        return {
            "usage_guidelines": {
                "when_to_use": "Clear use cases",
                "when_not_to_use": "Anti-patterns",
                "accessibility": "WCAG guidelines"
            },
            "code_examples": {
                "html": True,
                "css": True,
                "javascript": True
            },
            "props_api": {
                "properties": True,
                "events": True,
                "slots": True
            }
        }

    def _define_foundations(self) -> Dict:
        return {
            "grid_system": {
                "columns": 12,
                "gutters": "24px",
                "margins": "16px",
                "breakpoints": ["576px", "768px", "992px", "1200px"]
            },
            "motion": {
                "duration": {
                    "quick": "100ms",
                    "normal": "200ms",
                    "slow": "300ms"
                },
                "easing": {
                    "ease_out": "cubic-bezier(0.4, 0, 0.2, 1)",
                    "ease_in": "cubic-bezier(0.4, 0, 1, 1)",
                    "sharp": "cubic-bezier(0.4, 0, 0.6, 1)"
                }
            }
        }

    def _define_component_library(self) -> Dict:
        return {
            "inputs": ["Text", "Select", "Checkbox", "Radio"],
            "navigation": ["Menu", "Tabs", "Breadcrumbs"],
            "feedback": ["Alert", "Toast", "Modal"],
            "layout": ["Grid", "Card", "Container"]
        }

    def _define_design_patterns(self) -> Dict:
        return {
            "navigation": {
                "hierarchy": "Clear visual hierarchy",
                "wayfinding": "Breadcrumbs and navigation",
                "search": "Global search functionality"
            },
            "forms": {
                "validation": "Inline validation",
                "error_handling": "Clear error messages",
                "success_feedback": "Confirmation messages"
            }
        }

    def _create_guidelines(self) -> Dict:
        return {
            "accessibility": {
                "color_contrast": "WCAG AA compliance",
                "keyboard_navigation": "Full keyboard support",
                "screen_readers": "ARIA labels and roles"
            },
            "responsive_design": {
                "mobile_first": "Progressive enhancement",
                "breakpoints": "Standard breakpoints",
                "touch_targets": "Minimum 44x44px"
            }
        }

    def _create_design_resources(self) -> Dict:
        return {
            "design_tokens": {
                "colors": "Color system",
                "typography": "Type scale",
                "spacing": "Spacing scale"
            },
            "assets": {
                "icons": "Icon library",
                "illustrations": "Illustration library",
                "templates": "Page templates"
            }
        }

    def _design_screens(self) -> List[Dict]:
        return [
            {
                "name": "Dashboard",
                "layout": "Grid layout",
                "components": ["Header", "Sidebar", "Content Area"],
                "states": ["Default", "Loading", "Empty"]
            },
            {
                "name": "Profile",
                "layout": "Single column",
                "components": ["Avatar", "Info Form", "Activity Feed"],
                "states": ["View", "Edit", "Saving"]
            }
        ]

    def _define_interactions(self) -> Dict:
        return {
            "navigation": {
                "click": "Page transition",
                "hover": "Visual feedback",
                "active": "State change"
            },
            "forms": {
                "input": "Real-time validation",
                "submit": "Loading state",
                "success": "Confirmation animation"
            }
        }

    def _define_animations(self) -> Dict:
        return {
            "page_transitions": {
                "enter": "Fade in",
                "exit": "Fade out",
                "duration": "300ms"
            },
            "component_animations": {
                "mount": "Scale up",
                "unmount": "Scale down",
                "duration": "200ms"
            }
        }

    def _prepare_assets(self) -> Dict:
        return {
            "images": {
                "formats": ["SVG", "PNG", "WebP"],
                "sizes": ["1x", "2x", "3x"],
                "optimization": "Compressed"
            },
            "icons": {
                "formats": ["SVG", "Icon font"],
                "sizes": ["16px", "24px", "32px"],
                "styles": ["Outlined", "Filled"]
            }
        }

    def _create_specifications(self) -> Dict:
        return {
            "layout_specs": {
                "dimensions": "Exact measurements",
                "spacing": "Margin and padding",
                "alignment": "Grid alignment"
            },
            "interaction_specs": {
                "states": "Component states",
                "transitions": "Animation timing",
                "behaviors": "Interactive behaviors"
            }
        }


if __name__ == "__main__":
    # Test the InterfaceDesigner tool
    test_spec = {
        "brand": {
            "colors": {
                "primary": "#007AFF",
                "secondary": "#00C853"
            },
            "typography": {
                "primary_font": "Inter",
                "secondary_font": "Roboto"
            }
        },
        "requirements": {
            "accessibility": "WCAG AA",
            "responsive": True,
            "themes": ["light", "dark"]
        }
    }
    
    designer = InterfaceDesigner(
        design_spec=test_spec,
        design_type="visual",
        platform="web"
    )
    
    print("Testing InterfaceDesigner tool:")
    print(designer.run()) 