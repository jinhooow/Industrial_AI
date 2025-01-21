from durable.lang import *

with (ruleset('autonomous_driving')):
    # 1. operator 컴퓨터의 전원을 킨다
    @when_all((m.action == 'turn_on') & (m.device == 'operator_computer'))
    def turn_on_operator_computer(c):
        c.assert_fact({'direct': 'output', 'subject': 'operator_computer', 'predicate': 'power', 'object': 'on'})

    # 2. 휠 레이싱 자동차 게임기를 연결한다
    @when_all((m.action == 'connect') & (m.device == 'wheel_racing_game_console'))
    def connect_wheel_racing_game_console(c):
        c.assert_fact({'direct': 'output', 'subject': 'wheel_racing_game_console', 'predicate': 'connection', 'object': 'connected'})

    # 3. ToD_S/W를 실행한다
    @when_all((m.action == 'run') & (m.software == 'ToD_Software'))
    def run_ToD_Software(c):
        c.assert_fact({'direct': 'output', 'subject': 'ToD_Software', 'predicate': 'execution', 'object': 'executed'})

    # 4. 자동차의 시동을 건다
    @when_all((m.action == 'start_engine') & (m.device == 'car'))
    def start_engine(c):
        c.assert_fact({'direct': 'output', 'subject': 'car', 'predicate': 'ignition', 'object': 'started'})

    # 5. 자동차의 인버터, 제어전원 버튼을 순서대로 누른다.
    @when_all((m.action == 'press_button') & (m.device == 'car_inverter') & (m.order == 'first'))
    def press_inverter_button(c):
        c.assert_fact({'direct': 'output', 'subject': 'car_inverter', 'predicate': 'button', 'object': 'pressed'})

    @when_all((m.action == 'press_button') & (m.device == 'car_control_power') & (m.order == 'second'))
    def press_control_power_button(c):
        c.assert_fact({'direct': 'output', 'subject': 'car_control_power', 'predicate': 'button', 'object': 'pressed'})

    # 6. 자동차의 컴퓨터 전원을 킨다.
    @when_all((m.action == 'turn_on') & (m.device == 'car_computer'))
    def turn_on_car_computer(c):
        c.assert_fact({'direct': 'output', 'subject': 'car_computer', 'predicate': 'power', 'object': 'on'})

    # 7. 자동차의 전방, 후방, 좌,우 카메라가 잘 나오는지 확인한다.
    @when_all((m.action == 'check_camera') & (m.device == 'car_camera'))
    def check_car_camera(c):
        c.assert_fact({'direct': 'output', 'subject': 'car_camera', 'predicate': 'check', 'object': 'ok'})

    # 8. 카메라가 안나오면 컴퓨터를 껏다 킨다.
    @when_all((m.action == 'restart_computer') & (m.device == 'car_computer') & (m.camera_status == 'not_ok'))
    def restart_car_computer(c):
        c.assert_fact({'direct': 'output', 'subject': 'car_computer', 'predicate': 'restart', 'object': 'restarted'})

    # 9. 자동차의 ToD_S/W를 실행한다.
    @when_all((m.action == 'run') & (m.software == 'ToD_Software') & (m.device == 'car_computer'))
    def run_ToD_Software_car(c):
        c.assert_fact({'direct': 'output', 'subject': 'car_computer', 'predicate': 'execution', 'object': 'executed'})

    # 10. operator 컴퓨터와의 연결을 시도한다.
    @when_all((m.action == 'connect') & (m.device == 'operator_computer'))
    def connect_operator_computer(c):
        c.assert_fact({'direct': 'output', 'subject': 'operator_computer', 'predicate': 'connection', 'object': 'connected'})

    # 11. 연결이 안될 시 operator의 IP와 차량컴퓨터의 네트워크 상태를 확인한다.
    @when_all((m.action == 'check_network') & (m.device == 'operator_computer') & (m.connection_status == 'not_connected'))
    def check_network_status(c):
        c.assert_fact({'direct': 'output', 'subject': 'network_status', 'predicate': 'check', 'object': 'not_connected'})

    # 12. 연결이되면 출발 전 operator의 움직임에 따라 핸들과 브레이크가 작동하는지 확인한다.
    @when_all((m.action == 'check_controls') & (m.device == 'car') & (m.operator_movement == 'yes'))
    def check_controls(c):
        c.assert_fact({'direct': 'output', 'subject': 'car_controls', 'predicate': 'check', 'object': 'ok'})

    # 13 안전을 위해 operator와 차량의 운전자들 끼리 전화를 한다.
    @when_all((m.action == 'call') & (m.party == 'driver') & (m.device == 'phone'))
    def call_driver(c):
        c.assert_fact({'direct': 'output', 'subject': 'phone', 'predicate': 'call', 'object': 'driver'})

    # 14. 작동이 된다면 기어를 변경 후 천천히 이동한다.
    @when_all((m.action == 'change_gear') & (m.device == 'car'))
    def change_gear(c):
        c.assert_fact({'direct': 'output', 'subject': 'car', 'predicate': 'gear', 'object': 'changed'})

    # 15. 조작이 미흡하거나 위급상황시 차량의 운전자는 브레이크 밟을 준비를 한다.
    @when_all((m.action == 'prepare_brake') & (m.device == 'car_driver'))
    def prepare_brake(c):
        c.assert_fact({'direct': 'output', 'subject': 'car_driver', 'predicate': 'prepare', 'object': 'brake'})

    # 결과 출력 함수
    @when_all(+m.subject)
    def output(c):
        print('{0}: {1} {2} {3}'.format(c.m.direct, c.m.subject, c.m.predicate, c.m.object))

# 초기 사실 주입
assert_fact('autonomous_driving', {'action': 'turn_on', 'device': 'operator_computer'})
assert_fact('autonomous_driving', {'action': 'connect', 'device': 'wheel_racing_game_console'})
assert_fact('autonomous_driving', {'action': 'run', 'software': 'ToD_Software'})
assert_fact('autonomous_driving', {'action': 'start_engine', 'device': 'car'})
assert_fact('autonomous_driving', {'action': 'press_button', 'device': 'car_inverter', 'order': 'first'})
assert_fact('autonomous_driving', {'action': 'press_button', 'device': 'car_control_power', 'order': 'second'})
assert_fact('autonomous_driving', {'action': 'turn_on', 'device': 'car_computer'})
assert_fact('autonomous_driving', {'action': 'check_camera', 'device': 'car_camera'})
assert_fact('autonomous_driving', {'action': 'restart_computer', 'device': 'car_computer', 'camera_status': 'not_ok'})
assert_fact('autonomous_driving', {'action': 'run', 'software': 'ToD_Software', 'device': 'car_computer'})
assert_fact('autonomous_driving', {'action': 'connect', 'device': 'operator_computer'})
assert_fact('autonomous_driving', {'action': 'check_network', 'device': 'operator_computer', 'connection_status': 'not_connected'})
assert_fact('autonomous_driving', {'action': 'check_controls', 'device': 'car', 'operator_movement': 'yes'})
assert_fact('autonomous_driving', {'action': 'call', 'party': 'driver', 'device': 'phone'})
assert_fact('autonomous_driving', {'action': 'change_gear', 'device': 'car'})
assert_fact('autonomous_driving', {'action': 'prepare_brake', 'device': 'car_driver'})